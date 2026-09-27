import streamlit as st
import requests


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ELORA - Food Barcode Scanner",
    page_icon="",
    layout="wide"
)


# =========================================================
# THEME
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #F7F7F7;
        color: #111111;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #111111 !important;
    }

    p, label {
        color: #333333;
    }

    [data-testid="stSidebar"] {
        background-color: #111111;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    .stButton > button {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #111111 !important;
        border-radius: 10px;
        padding: 0.55rem 1.2rem;
        font-weight: 500;
    }

    .stButton > button p {
        color: #FFFFFF !important;
    }

    .stButton > button:hover {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #111111 !important;
    }

    .stButton > button:hover p {
        color: #111111 !important;
    }

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5 !important;
        border-radius: 8px;
    }

    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E2E2;
        border-radius: 12px;
        padding: 15px;
    }

    [data-testid="stMetricLabel"] {
        color: #666666 !important;
    }

    [data-testid="stMetricValue"] {
        color: #111111 !important;
    }

    hr {
        border-color: #E0E0E0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "barcode_mode" not in st.session_state:
    st.session_state.barcode_mode = "manual"

if "barcode_product" not in st.session_state:
    st.session_state.barcode_product = None

if "barcode_value" not in st.session_state:
    st.session_state.barcode_value = ""

if "barcode_product_type" not in st.session_state:
    st.session_state.barcode_product_type = ""


# =========================================================
# UNIVERSAL PRODUCT LOOKUP
# =========================================================

def lookup_barcode(barcode):

    barcode = str(barcode).strip()

    if not barcode:
        return None, None, "Please enter a barcode."

    url = (
        "https://world.openfoodfacts.org/api/v3/product/"
        + barcode
    )

    params = {
        "product_type": "all",
        "cc": "ae",
        "lc": "en",
        "fields": "all"
    }

    headers = {
        "User-Agent":
        "ELORA-Health-Nutrition/1.0"
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=20,
            allow_redirects=True
        )

        if response.status_code == 404:

            return (
                None,
                None,
                "Barcode detected, but no matching product was found."
            )

        if response.status_code != 200:

            return (
                None,
                None,
                "The product database could not be reached."
            )

        data = response.json()

        product = data.get("product")

        if not product:

            return (
                None,
                None,
                "Barcode detected, but no matching product was found."
            )

        product_type = (
            product.get("product_type")
            or ""
        )

        return product, product_type, None

    except requests.exceptions.RequestException:

        return (
            None,
            None,
            "Could not connect to the product database."
        )

    except Exception:

        return (
            None,
            None,
            "Something went wrong while looking up the barcode."
        )


# =========================================================
# BARCODE CAMERA COMPONENT
# =========================================================

barcode_camera = st.components.v2.component(
    name="elora_barcode_camera",

    html="""
    <div class="scanner">

        <video
            id="barcode-video"
            autoplay
            muted
            playsinline>
        </video>

        <div class="scan-frame">

            <div class="corner top-left"></div>
            <div class="corner top-right"></div>
            <div class="corner bottom-left"></div>
            <div class="corner bottom-right"></div>

        </div>

        <div id="scanner-status">
            Starting camera...
        </div>

    </div>
    """,

    css="""
    .scanner {
        position: relative;
        width: 100%;
        max-width: 700px;
        margin: 0 auto;
        background: #111111;
        border-radius: 16px;
        overflow: hidden;
    }

    #barcode-video {
        width: 100%;
        height: 420px;
        object-fit: cover;
        display: block;
        background: #111111;
    }

    .scan-frame {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 72%;
        height: 130px;
        transform: translate(-50%, -50%);
        pointer-events: none;
    }

    .corner {
        position: absolute;
        width: 35px;
        height: 35px;
        border-color: #FFFFFF;
        border-style: solid;
    }

    .top-left {
        top: 0;
        left: 0;
        border-width: 3px 0 0 3px;
    }

    .top-right {
        top: 0;
        right: 0;
        border-width: 3px 3px 0 0;
    }

    .bottom-left {
        bottom: 0;
        left: 0;
        border-width: 0 0 3px 3px;
    }

    .bottom-right {
        bottom: 0;
        right: 0;
        border-width: 0 3px 3px 0;
    }

    #scanner-status {
        position: absolute;
        bottom: 18px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 0, 0, 0.78);
        color: #FFFFFF;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        white-space: nowrap;
    }
    """,

    js="""
    export default function(component) {

        const {
            parentElement,
            setStateValue
        } = component;

        const video =
            parentElement.querySelector("#barcode-video");

        const status =
            parentElement.querySelector("#scanner-status");

        let controls = null;
        let stopped = false;
        let lastBarcode = "";

        async function loadZXing() {

            if (window.ZXingBrowser) {
                return window.ZXingBrowser;
            }

            return new Promise((resolve, reject) => {

                const oldScript =
                    document.querySelector(
                        'script[data-elora-zxing="true"]'
                    );

                if (oldScript) {

                    if (window.ZXingBrowser) {
                        resolve(window.ZXingBrowser);
                        return;
                    }

                    oldScript.addEventListener(
                        "load",
                        () => {
                            resolve(window.ZXingBrowser);
                        }
                    );

                    oldScript.addEventListener(
                        "error",
                        reject
                    );

                    return;
                }

                const script =
                    document.createElement("script");

                script.src =
                    "https://unpkg.com/@zxing/browser@0.2.1";

                script.async = true;

                script.dataset.eloraZxing = "true";

                script.onload = () => {

                    if (window.ZXingBrowser) {

                        resolve(
                            window.ZXingBrowser
                        );

                    } else {

                        reject(
                            new Error(
                                "ZXing was loaded but is unavailable."
                            )
                        );
                    }
                };

                script.onerror = () => {

                    reject(
                        new Error(
                            "Could not load ZXing."
                        )
                    );
                };

                document.head.appendChild(script);
            });
        }


        async function startScanner() {

            try {

                status.textContent =
                    "Loading barcode scanner...";

                const ZXingBrowser =
                    await loadZXing();

                if (stopped) {
                    return;
                }

                const reader =
                    new ZXingBrowser.BrowserMultiFormatReader();

                status.textContent =
                    "Starting camera...";

                controls =
                    await reader.decodeFromVideoDevice(
                        undefined,
                        video,
                        (result, error) => {

                            if (stopped) {
                                return;
                            }

                            if (result) {

                                const value =
                                    result.getText();

                                if (
                                    value &&
                                    value !== lastBarcode
                                ) {

                                    lastBarcode = value;

                                    status.textContent =
                                        "Barcode detected: " +
                                        value;

                                    setStateValue(
                                        "barcode",
                                        value
                                    );
                                }
                            }
                        }
                    );

                if (!stopped) {

                    status.textContent =
                        "Point your camera at a barcode";

                }

            } catch (error) {

                console.error(
                    "ELORA scanner error:",
                    error
                );

                status.textContent =
                    "Could not start camera scanner.";
            }
        }


        startScanner();


        return () => {

            stopped = true;

            if (controls) {

                try {
                    controls.stop();
                } catch (error) {
                    console.log(error);
                }
            }

            if (
                video &&
                video.srcObject
            ) {

                const tracks =
                    video.srcObject.getTracks();

                tracks.forEach(
                    track => track.stop()
                );

                video.srcObject = null;
            }
        };
    }
    """
)


# =========================================================
# HEADER
# =========================================================

st.caption("ELORA")

st.title("FOOD BARCODE SCANNER")

st.write(
    "Scan or enter a barcode to identify a product "
    "and view the information available for it."
)

st.write("")


# =========================================================
# SEARCH MODE
# =========================================================

st.subheader("How would you like to search?")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "📷 Camera Scanner",
        use_container_width=True
    ):

        st.session_state.barcode_mode = "camera"

        st.session_state.barcode_product = None

        st.session_state.barcode_product_type = ""


with col2:

    if st.button(
        "⌨️ Manual Entry",
        use_container_width=True
    ):

        st.session_state.barcode_mode = "manual"


st.write("")


# =========================================================
# CAMERA MODE
# =========================================================

if st.session_state.barcode_mode == "camera":

    st.markdown("### CAMERA SCANNER")

    st.write(
        "Allow camera access and place the barcode "
        "inside the scanning frame."
    )

    camera_result = barcode_camera(
        key="elora_camera_scanner",
        on_barcode_change=lambda: None
    )

    detected_barcode = getattr(
        camera_result,
        "barcode",
        None
    )

    if detected_barcode:

        detected_barcode = str(
            detected_barcode
        ).strip()

        if detected_barcode:

            if (
                detected_barcode
                != st.session_state.barcode_value
            ):

                st.session_state.barcode_value = (
                    detected_barcode
                )

                with st.spinner(
                    "Identifying product..."
                ):

                    product, product_type, error = (
                        lookup_barcode(
                            detected_barcode
                        )
                    )

                if product:

                    st.session_state.barcode_product = (
                        product
                    )

                    st.session_state.barcode_product_type = (
                        product_type
                    )

                    st.success(
                        f"Barcode detected: {detected_barcode}"
                    )

                else:

                    st.warning(error)


# =========================================================
# MANUAL MODE
# =========================================================

else:

    st.markdown("### FIND A PRODUCT")

    st.write(
        "Enter the product barcode below."
    )

    barcode = st.text_input(
        "Barcode",
        placeholder="Example: 8886467116742",
        label_visibility="collapsed"
    )

    search_button = st.button(
        "Search Product",
        use_container_width=True
    )

    if search_button:

        barcode = barcode.strip()

        if not barcode:

            st.warning(
                "Please enter a barcode."
            )

        else:

            with st.spinner(
                "Identifying product..."
            ):

                product, product_type, error = (
                    lookup_barcode(
                        barcode
                    )
                )

            if product:

                st.session_state.barcode_product = (
                    product
                )

                st.session_state.barcode_product_type = (
                    product_type
                )

                st.session_state.barcode_value = (
                    barcode
                )

            else:

                st.session_state.barcode_product = None

                st.warning(error)


# =========================================================
# PRODUCT DISPLAY
# =========================================================

product = st.session_state.barcode_product

product_type = (
    st.session_state.barcode_product_type
)


if product:

    st.divider()

    # -----------------------------------------------------
    # PRODUCT NAME
    # -----------------------------------------------------

    product_name = (
        product.get("product_name_en")
        or product.get("product_name")
        or product.get("generic_name_en")
        or product.get("generic_name")
        or "Unknown Product"
    )

    # -----------------------------------------------------
    # BRAND
    # -----------------------------------------------------

    brand = (
        product.get("brands")
        or product.get("brand_owner")
        or product.get("manufacturer")
        or "Not available"
    )

    # -----------------------------------------------------
    # CATEGORY
    # -----------------------------------------------------

    category = ""

    categories_en = product.get(
        "categories_en"
    )

    if categories_en:

        if isinstance(
            categories_en,
            list
        ):

            category = categories_en[0]

        else:

            category = str(
                categories_en
            ).split(",")[0].strip()

    if not category:

        categories = product.get(
            "categories"
        )

        if categories:

            if isinstance(
                categories,
                list
            ):

                category = categories[0]

            else:

                category = str(
                    categories
                ).split(",")[0].strip()

    if not category:

        category_tags = product.get(
            "categories_tags"
        )

        if category_tags:

            if isinstance(
                category_tags,
                list
            ):

                category = category_tags[0]

            else:

                category = str(
                    category_tags
                ).split(",")[0].strip()

    if category:

        category = str(
            category
        )

        category = category.replace(
            "en:",
            ""
        )

        category = category.replace(
            "-",
            " "
        )

        category = category.replace(
            "_",
            " "
        )

        category = category.strip().title()

    else:

        category = "Not available"

    # -----------------------------------------------------
    # QUANTITY
    # -----------------------------------------------------

    quantity = product.get(
        "quantity",
        "Not available"
    )

    # -----------------------------------------------------
    # BARCODE
    # -----------------------------------------------------

    barcode_code = (
        product.get("code")
        or st.session_state.barcode_value
        or "Not available"
    )

    # -----------------------------------------------------
    # PRODUCT TYPE
    # -----------------------------------------------------

    type_names = {
        "food": "Food",
        "beauty": "Beauty / Personal Care",
        "petfood": "Pet Food",
        "product": "General Product"
    }

    display_type = type_names.get(
        product_type,
        "Product"
    )

    # -----------------------------------------------------
    # PRODUCT HEADER
    # -----------------------------------------------------

    st.header(product_name)

    st.caption(
        f"Product type: {display_type}"
    )

    st.write("")

    info1, info2, info3 = st.columns(3)

    with info1:

        st.metric(
            "Brand",
            brand
        )

    with info2:

        st.metric(
            "Category",
            category
        )

    with info3:

        st.metric(
            "Quantity",
            quantity
        )

    st.caption(
        f"Barcode: {barcode_code}"
    )

    st.write("")


    # =====================================================
    # PRODUCT IMAGE
    # =====================================================

    image_url = (
        product.get("image_front_url")
        or product.get("image_url")
        or product.get("image_small_url")
    )

    if image_url:

        try:

            st.image(
                image_url,
                width=300
            )

        except Exception:

            pass


    # =====================================================
    # DESCRIPTION
    # =====================================================

    description = (
        product.get("generic_name_en")
        or product.get("generic_name")
        or product.get("description")
    )

    if description:

        st.subheader(
            "Product Information"
        )

        st.write(
            description
        )


    # =====================================================
    # MANUFACTURER
    # =====================================================

    manufacturer = (
        product.get("manufacturer")
        or product.get("manufacturing_places")
        or product.get("brand_owner")
    )

    if manufacturer:

        st.subheader(
            "Manufacturer"
        )

        st.write(
            manufacturer
        )


    # =====================================================
    # NUTRI-SCORE
    # =====================================================

    nutri_score = (
        product.get("nutriscore_grade")
        or product.get("nutrition_grades")
    )

    if nutri_score:

        score = str(
            nutri_score
        ).strip().lower()

        score_colors = {
            "a": ("#168A42", "#FFFFFF"),
            "b": ("#85BB2F", "#FFFFFF"),
            "c": ("#F7D64A", "#111111"),
            "d": ("#EE8A24", "#FFFFFF"),
            "e": ("#D71920", "#FFFFFF")
        }

        if score in score_colors:

            background, text_color = (
                score_colors[score]
            )

            st.subheader(
                "Nutri-Score"
            )

            st.markdown(
                f"""
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    margin:10px 0 25px 0;
                ">
                    <div style="
                        width:75px;
                        height:75px;
                        border-radius:14px;
                        background:{background};
                        color:{text_color};
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        font-size:40px;
                        font-weight:800;
                    ">
                        {score.upper()}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


    # =====================================================
    # NUTRITION INFORMATION
    # =====================================================

    nutriments = product.get(
        "nutriments",
        {}
    )

    if nutriments:

        st.subheader(
            "Nutrition Information"
        )

        calories = (
            nutriments.get(
                "energy-kcal_100g"
            )
            or
            nutriments.get(
                "energy-kcal"
            )
        )

        carbohydrates = nutriments.get(
            "carbohydrates_100g"
        )

        protein = nutriments.get(
            "proteins_100g"
        )

        fat = nutriments.get(
            "fat_100g"
        )

        fiber = nutriments.get(
            "fiber_100g"
        )

        sugar = nutriments.get(
            "sugars_100g"
        )

        salt = nutriments.get(
            "salt_100g"
        )

        saturated_fat = nutriments.get(
            "saturated-fat_100g"
        )


        def grams(value):

            if value is None:
                return "—"

            try:

                return f"{float(value):.1f} g"

            except:

                return str(value)


        nutrition1, nutrition2, nutrition3 = (
            st.columns(3)
        )

        with nutrition1:

            if calories is not None:

                try:

                    st.metric(
                        "Calories / 100g",
                        f"{float(calories):.0f} kcal"
                    )

                except:

                    st.metric(
                        "Calories / 100g",
                        str(calories)
                    )

            else:

                st.metric(
                    "Calories / 100g",
                    "—"
                )

            st.metric(
                "Carbohydrates",
                grams(carbohydrates)
            )


        with nutrition2:

            st.metric(
                "Protein",
                grams(protein)
            )

            st.metric(
                "Fat",
                grams(fat)
            )


        with nutrition3:

            st.metric(
                "Fiber",
                grams(fiber)
            )

            st.metric(
                "Sugar",
                grams(sugar)
            )


        if saturated_fat is not None:

            st.metric(
                "Saturated Fat / 100g",
                grams(saturated_fat)
            )


        if salt is not None:

            st.metric(
                "Salt / 100g",
                grams(salt)
            )


    # =====================================================
    # INGREDIENTS
    # =====================================================

    ingredients = (
        product.get(
            "ingredients_text_en"
        )
        or
        product.get(
            "ingredients_text"
        )
    )

    if ingredients:

        st.subheader(
            "Ingredients"
        )

        st.write(
            ingredients
        )


    # =====================================================
    # ALLERGENS
    # =====================================================

    allergens = (
        product.get(
            "allergens_en"
        )
        or
        product.get(
            "allergens"
        )
    )

    if allergens:

        st.subheader(
            "Allergens"
        )

        st.write(
            allergens
        )


    # =====================================================
    # ADDITIONAL PRODUCT DETAILS
    # =====================================================

    countries = (
        product.get(
            "countries_en"
        )
        or
        product.get(
            "countries"
        )
    )

    if countries:

        st.subheader(
            "Additional Information"
        )

        st.write(
            f"Countries: {countries}"
        )


    # =====================================================
    # NUTRITION OVERVIEW
    # =====================================================

    if nutriments:

        st.subheader(
            "Nutrition Overview"
        )

        notes = []

        if sugar is not None:

            try:

                if float(sugar) >= 10:

                    notes.append(
                        "The product contains a relatively high amount of sugar per 100g."
                    )

            except:

                pass

        if salt is not None:

            try:

                if float(salt) >= 1.5:

                    notes.append(
                        "The product contains a relatively high amount of salt per 100g."
                    )

            except:

                pass

        if protein is not None:

            try:

                if float(protein) >= 5:

                    notes.append(
                        "The product provides a measurable amount of protein."
                    )

            except:

                pass

        if fiber is not None:

            try:

                if float(fiber) >= 3:

                    notes.append(
                        "The product provides a useful amount of dietary fiber."
                    )

            except:

                pass


        if notes:

            for note in notes:

                st.write(
                    "• " + note
                )

        else:

            st.write(
                "Additional nutrition observations "
                "are not available."
            )


    # =====================================================
    # SOURCE
    # =====================================================

    st.caption(
        "Product information is retrieved from the "
        "Open Food Facts ecosystem. Available information "
        "depends on the product record."
    )


# =========================================================
# FOOTER
# =========================================================

st.write("")

st.divider()

st.caption(
    "ELORA · Food Barcode Scanner"
)