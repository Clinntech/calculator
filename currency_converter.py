import requests
import streamlit as st
import pycountry


BASE_URL = "https://open.er-api.com/v6/latest"


def get_currency_name(currency_code):
    """Return the official name of an ISO currency code."""
    currency = pycountry.currencies.get(alpha_3=currency_code)

    if currency:
        return currency.name

    return currency_code


@st.cache_data(ttl=86400)
def get_supported_currencies():
    """
    Return currencies supported by the live exchange-rate API.

    Currency names are retrieved from the ISO 4217 currency list
    provided by pycountry.
    """
    try:
        response = requests.get(
            f"{BASE_URL}/USD",
            timeout=15,
        )
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            raise ConnectionError(
                "The currency service returned an unsuccessful response."
            )

        rates = data.get("rates", {})

        if not rates:
            raise ConnectionError(
                "No currencies were returned by the currency service."
            )

        return {
            code: get_currency_name(code)
            for code in rates.keys()
        }

    except requests.RequestException as error:
        raise ConnectionError(
            "Unable to load currencies. Check your internet connection."
        ) from error


@st.cache_data(ttl=3600)
def get_exchange_rates():
    """Retrieve the latest available currency exchange rates."""
    try:
        response = requests.get(
            f"{BASE_URL}/USD",
            timeout=15,
        )
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            raise ConnectionError(
                "The currency service returned an unsuccessful response."
            )

        rates = data.get("rates", {})

        if not rates:
            raise ConnectionError(
                "No exchange rates were returned."
            )

        return {
            "rates": rates,
            "date": data.get(
                "time_last_update_utc",
                "Latest available rate",
            ),
        }

    except requests.RequestException as error:
        raise ConnectionError(
            "Unable to retrieve exchange rates. "
            "Check your internet connection."
        ) from error


def convert_currency(amount, source_currency, target_currency):
    """
    Convert an amount between two supported currencies.

    All rates use USD as their common reference currency.
    """
    if amount < 0:
        raise ValueError("The amount cannot be negative.")

    if source_currency == target_currency:
        return {
            "converted_amount": amount,
            "exchange_rate": 1.0,
            "date": "Current",
        }

    rate_information = get_exchange_rates()
    rates = rate_information["rates"]

    if source_currency not in rates:
        raise ValueError(
            f"{source_currency} is not supported."
        )

    if target_currency not in rates:
        raise ValueError(
            f"{target_currency} is not supported."
        )

    source_rate = rates[source_currency]
    target_rate = rates[target_currency]

    exchange_rate = target_rate / source_rate
    converted_amount = amount * exchange_rate

    return {
        "converted_amount": converted_amount,
        "exchange_rate": exchange_rate,
        "date": rate_information["date"],
    }