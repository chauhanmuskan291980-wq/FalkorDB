
import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="TraceGuard AI",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 TraceGuard AI")
st.subheader("Evidence-backed Fraud Investigation")
st.caption(
    "Investigate account relationships using graph evidence powered by FalkorDB."
)

account_id = st.text_input(
    "Account ID",
    value="ACC-001",
    placeholder="Example: ACC-001",
)

if st.button("Investigate Account", type="primary"):
    if not account_id.strip():
        st.warning("Please enter an account ID.")
    else:
        with st.spinner("Querying the investigation API..."):
            try:
                response = requests.get(
                    f"{API_BASE_URL}/investigations/{account_id.strip()}",
                    timeout=15,
                )
                response.raise_for_status()
                data = response.json()

                evidence = data["evidence"]
                summary = data["summary"]
                report = data["report"]

                st.success(f"Investigation loaded for {data['account_id']}")

                col1, col2 = st.columns(2)

                col1.metric(
                    "Flagged Transactions",
                    summary["flagged_transaction_count"],
                )
                col2.metric(
                    "Shared-Device Connections",
                    summary["shared_device_connection_count"],
                )

                st.divider()
                st.header("Investigation Findings")

                if report["findings"]:
                    for finding in report["findings"]:
                        with st.expander(
                            finding["type"].replace("_", " ").title(),
                            expanded=True,
                        ):
                            st.write(finding["description"])
                            st.json(finding["evidence"])
                else:
                    st.info("No matching findings were returned.")

                st.header("Flagged Transactions")
                if evidence["flagged_transactions"]:
                    st.dataframe(
                        evidence["flagged_transactions"],
                        use_container_width=True,
                    )
                else:
                    st.info("No flagged transactions found.")

                st.header("Shared Devices")
                if evidence["shared_devices"]:
                    st.dataframe(
                        evidence["shared_devices"],
                        use_container_width=True,
                    )
                else:
                    st.info("No shared-device connections found.")

                st.header("Investigation Conclusion")
                st.write(report["conclusion"])

                st.caption(
                    "Risk indicators warrant review but do not independently "
                    "establish fraud."
                )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to the API. Start FastAPI first in "
                    "another terminal."
                )
            except requests.exceptions.Timeout:
                st.error("The API request timed out. Please try again.")
            except requests.exceptions.HTTPError as exc:
                st.error(f"The API returned an error: {exc}")
            except (KeyError, ValueError) as exc:
                st.error(f"The API response was not in the expected format: {exc}")
