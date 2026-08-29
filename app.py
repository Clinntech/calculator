import streamlit as st

from calculator import add, subtract, multiply, divide
from currency_converter import get_supported_currencies, convert_currency


st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed",
)


def load_css(file_path):
    """Load the application's custom CSS."""
    try:
        with open(file_path, encoding="utf-8") as css_file:
            st.markdown(
                f"<style>{css_file.read()}</style>",
                unsafe_allow_html=True,
            )
    except FileNotFoundError:
        pass


def format_number(number):
    """Display numbers without unnecessary decimal places."""
    return f"{number:,.6f}".rstrip("0").rstrip(".")


load_css("assets/style.css")


st.markdown(
    """
    <div class="app-header">
        <div class="brand-icon">C</div>
        <div>
            <h1>Calculator</h1>
            <p>Fast, accurate calculations for business and finance.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


calculator_tab, currency_tab = st.tabs(
    ["Calculator", "Currency Converter"]
)


with calculator_tab:
    st.markdown(
        '<p class="section-label">ENTER VALUES</p>',
        unsafe_allow_html=True,
    )

    first_column, second_column = st.columns(2)

    with first_column:
        first_number = st.number_input(
            "First number",
            value=0.0,
            format="%.6f",
            key="first_number",
        )

    with second_column:
        second_number = st.number_input(
            "Second number",
            value=0.0,
            format="%.6f",
            key="second_number",
        )

    st.markdown(
        '<p class="section-label">SELECT OPERATION</p>',
        unsafe_allow_html=True,
    )

    add_column, subtract_column, multiply_column, divide_column = st.columns(4)

    selected_operation = None

    with add_column:
        if st.button(
            "+",
            key="add_button",
            use_container_width=True,
            help="Addition",
        ):
            selected_operation = "add"

    with subtract_column:
        if st.button(
            "−",
            key="subtract_button",
            use_container_width=True,
            help="Subtraction",
        ):
            selected_operation = "subtract"

    with multiply_column:
        if st.button(
            "×",
            key="multiply_button",
            use_container_width=True,
            help="Multiplication",
        ):
            selected_operation = "multiply"

    with divide_column:
        if st.button(
            "÷",
            key="divide_button",
            use_container_width=True,
            help="Division",
        ):
            selected_operation = "divide"

    if selected_operation:
        try:
            if selected_operation == "add":
                result = add(first_number, second_number)
                symbol = "+"

            elif selected_operation == "subtract":
                result = subtract(first_number, second_number)
                symbol = "−"

            elif selected_operation == "multiply":
                result = multiply(first_number, second_number)
                symbol = "×"

            else:
                result = divide(first_number, second_number)
                symbol = "÷"

            st.markdown(
                f"""
                <div class="result-card">
                    <span class="result-label">RESULT</span>
                    <span class="calculation">
                        {format_number(first_number)}
                        {symbol}
                        {format_number(second_number)}
                    </span>
                    <strong>{format_number(result)}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

        except ZeroDivisionError:
            st.error(
                "Division by zero is not allowed. "
                "Enter a non-zero second number."
            )

        except (TypeError, ValueError):
            st.error("Please enter valid numbers and try again.")


with currency_tab:
    st.markdown(
        '<p class="section-label">LIVE CURRENCY CONVERTER</p>',
        unsafe_allow_html=True,
    )

    try:
        currencies = get_supported_currencies()
        currency_codes = sorted(currencies.keys())

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            value=1.0,
            step=1.0,
            format="%.2f",
            key="currency_amount",
        )

        source_column, target_column = st.columns(2)

        with source_column:
            source_currency = st.selectbox(
                "From",
                currency_codes,
                index=currency_codes.index("USD"),
                format_func=lambda code: f"{code} · {currencies[code]}",
            )

        with target_column:
            default_target = "KES" if "KES" in currency_codes else "EUR"

            target_currency = st.selectbox(
                "To",
                currency_codes,
                index=currency_codes.index(default_target),
                format_func=lambda code: f"{code} · {currencies[code]}",
            )

        if st.button(
            "Convert currency",
            type="primary",
            use_container_width=True,
        ):
            conversion = convert_currency(
                amount,
                source_currency,
                target_currency,
            )

            converted_amount = conversion["converted_amount"]
            exchange_rate = conversion["exchange_rate"]
            rate_date = conversion["date"]

            st.markdown(
                f"""
                <div class="result-card currency-result">
                    <span class="result-label">CONVERTED AMOUNT</span>
                    <span class="calculation">
                        {format_number(amount)} {source_currency}
                    </span>
                    <strong>
                        {format_number(converted_amount)} {target_currency}
                    </strong>
                    <span class="exchange-rate">
                        1 {source_currency} =
                        {format_number(exchange_rate)} {target_currency}
                    </span>
                    <span class="rate-date">
                        Rate date: {rate_date}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    except ConnectionError as error:
        st.error(str(error))

    except Exception:
        st.error(
            "The currency service is temporarily unavailable. "
            "Please try again later."
        )