import requests
import streamlit as st


BASE_URL = "https://api.frankfurter.app"


@st.cache_data(ttl=86400)
def get_supported_currencies():
    """Return currencies supported by the exchange-rate service."""
    try:
        response = requests.get(
            f"{BASE_URL}/currencies",
            timeout=10,
        )
        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        raise ConnectionError(
            "Unable to load currencies. Check your internet connection."
        ) from error


@st.cache_data(ttl=3600)
def get_exchange_rate(source_currency, target_currency):
    """Return the latest rate between two currencies."""
    if source_currency == target_currency:
        return {
            "rate": 1.0,
            "date": "Current",
        }

    try:
        response = requests.get(
            f"{BASE_URL}/latest",
            params={
                "from": source_currency,
                "to": target_currency,
            },
            timeout=10,
        )
        response.raise_for_status()

        data = response.json()

        return {
            "rate": data["rates"][target_currency],
            "date": data["date"],
        }

    except requests.RequestException as error:
        raise ConnectionError(
            "Unable to retrieve the latest exchange rate. "
            "Check your internet connection."
        ) from error


def convert_currency(amount, source_currency, target_currency):
    """Convert an amount from one currency to another."""
    if amount < 0:
        raise ValueError("The amount cannot be negative.")

    rate_information = get_exchange_rate(
        source_currency,
        target_currency,
    )

    exchange_rate = rate_information["rate"]

    return {
        "converted_amount": amount * exchange_rate,
        "exchange_rate": exchange_rate,
        "date": rate_information["date"],
    }