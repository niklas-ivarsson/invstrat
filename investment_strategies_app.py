import streamlit as st

# === Lösenordsskydd ===
st.set_page_config(page_title="Investeringsstrategier", layout="wide")

#correct_password = st.secrets.get("app_password", None)  # Läggs in i .streamlit/secrets.toml
# hårdkodat, för att testa bara
correct_password = "15gastar1flaskarom"

password = st.text_input("🔒 Ange lösenord för att fortsätta", type="password")

if password != correct_password:
    st.warning("Fel lösenord. Försök igen.")
    st.stop()
    
st.set_page_config(page_title="Investeringsstrategier", layout="wide")

st.title("📊 Investeringsstrategier")

# === Sidomeny ===
menu = st.sidebar.radio(
    "Navigera:",
    ["Magic Formula", "Piotroski F-score", "📚 Lexikon"]
)

# === MAGIC FORMULA ===
if menu == "Magic Formula":
    st.header("📘 Magic Formula – Joel Greenblatt")
    
    # FLIKAR: Sammanfattning först
    tabs = st.tabs(["📌 Sammanfattning", "📈 Return on Capital", "💰 Earnings Yield"])

    # === SAMMANFATTNING ===
    with tabs[0]:
        st.subheader("📌 Sammanfattning")
        st.markdown("""
        Joel Greenblatt's **Magic Formula** combines two key metrics:

        1. ✅ **Return on Capital (ROC)** – to find **high-quality businesses**
        2. 💸 **Earnings Yield (Vinstavkastning)** – to find **undervalued stocks**

        Den magiska formeln syftar till att:
        - **Identifiera bra företag** (hög ROC)
        - **Köpa dem billigt** (hög Vinstavkastning)

        Rankningen sker genom att:
        - Alla bolag får ett ROC-rank (kvalitet)
        - Alla bolag får ett EY-rank (värdering)
        - Summera dessa ranker → lägst totalrank = mest attraktiv aktie
        """)

    # === RETURN ON CAPITAL ===
    with tabs[1]:
        st.subheader("📈 Return on Capital (ROC) / Avkastning på kapital")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### English")
            st.markdown("""
            **Definition:**  
            Return on Capital measures how efficiently a company generates profits from the capital it uses.

            **Formula:**  
            `ROC = EBIT / (Net Working Capital + Net Fixed Assets)`
            """)

            with st.expander("What is EBIT?"):
                st.write("EBIT = Earnings Before Interest and Taxes. It reflects the company’s core operational profitability.")

            with st.expander("What is Net Working Capital?"):
                st.write("Net Working Capital = Current Assets – Current Liabilities. It shows short-term financial health.")

            with st.expander("What are Net Fixed Assets?"):
                st.write("Long-term tangible assets (e.g., machinery, buildings) minus depreciation.")

        with col2:
            st.markdown("### Svenska")
            st.markdown("""
            **Definition:**  
            Avkastning på kapital visar hur effektivt ett företag genererar vinst från det kapital som används i verksamheten.

            **Formel:**  
            `ROC = Rörelseresultat (EBIT) / (Rörelsekapital + Anläggningstillgångar)`
            """)

            with st.expander("Vad är EBIT?"):
                st.write("EBIT = Rörelseresultat före räntor och skatt. Det visar hur lönsam kärnverksamheten är utan att ta hänsyn till finansiering eller skatt.")

            with st.expander("Vad är Rörelsekapital?"):
                st.write("Omsättningstillgångar minus kortfristiga skulder. Mäter företagets kortsiktiga finansiella balans.")

            with st.expander("Vad är Anläggningstillgångar?"):
                st.write("Långsiktiga tillgångar som maskiner, byggnader m.m., efter avskrivningar.")

    # === EARNINGS YIELD ===
    with tabs[2]:
        st.subheader("💰 Earnings Yield / Vinstavkastning")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### English")
            st.markdown("""
            **Definition:**  
            Earnings Yield indicates how cheap a stock is relative to its earnings. It’s the inverse of the P/E ratio.

            **Formula:**  
            `Earnings Yield = EBIT / Enterprise Value`
            """)

            with st.expander("What is EBIT?"):
                st.write("EBIT = Earnings Before Interest and Taxes. A measure of operating profit.")

            with st.expander("What is Enterprise Value?"):
                st.write("Enterprise Value = Market Cap + Total Debt – Cash. It represents the total value of the business.")

        with col2:
            st.markdown("### Svenska")
            st.markdown("""
            **Definition:**  
            Vinstavkastning visar hur billigt ett företag är i förhållande till sin vinst. Det är omvänt mot P/E-talet.

            **Formel:**  
            `Vinstavkastning = Rörelseresultat (EBIT) / Företagsvärde (Enterprise Value)`
            """)

            with st.expander("Vad är EBIT?"):
                st.write("EBIT = Rörelseresultat före räntor och skatt. Ett mått på operativ lönsamhet.")

            with st.expander("Vad är Företagsvärde?"):
                st.write("Företagsvärde = Börsvärde + Skulder – Kassa. Ett helhetsmått på värdet av verksamheten.")



# === PIOTROSKI F-SCORE ===
elif menu == "Piotroski F-score":
    st.header("📙 Piotroski F-score – Fundamentalanalys")

    tabs = st.tabs(["ℹ️ Vad är F-score?", "🧮 9 kriterier", "📌 Sammanfattning"])

    with tabs[0]:
        st.subheader("ℹ️ Vad är F-score?")
        st.markdown("""
        **F-score** utvecklades av professor **Joseph Piotroski** och är ett sätt att utvärdera företag baserat på deras finansiella hälsa.  
        Skalan går från **0 till 9**, där högre poäng betyder bättre finansiell styrka.

        Syftet är att identifiera undervärderade företag med **god lönsamhet, effektivitet och finansiell stabilitet**.
        """)

    with tabs[1]:
        st.subheader("🧮 De 9 kriterierna")
        st.markdown("""
        F-score baseras på tre kategorier:

        #### 1. **Lönsamhet (4 poäng)**
        - Positivt ROA (Return on Assets)
        - Positivt kassaflöde från verksamheten
        - Förbättrad ROA från föregående år
        - Kassaflöde > nettoresultat

        #### 2. **Finansiell styrka (3 poäng)**
        - Lägre skuldsättningsgrad
        - Högre likviditet (current ratio)
        - Inga nya aktier emitterade

        #### 3. **Effektivitet (2 poäng)**
        - Förbättrad bruttomarginal
        - Ökad kapitalomsättningshastighet
        """)

    with tabs[2]:
        st.subheader("📌 Sammanfattning")
        st.markdown("""
        ✅ Poängsättning från 0–9 där **7–9 = starkt bolag**, **0–3 = svagt bolag**.  
        ✅ Kombineras ofta med andra strategier som värdeinvestering eller Magic Formula.  
        ✅ Fungerar särskilt bra för småbolag enligt Piotroskis ursprungliga studie.
        """)
        
# === Lexikon ===
elif menu == "📚 Lexikon":
    st.header("📚 Finansiellt Lexikon")

    st.markdown("Skriv ett nyckelord för att filtrera:")

    search_query = st.text_input("🔍 Sök", "").strip().lower()

    # Finansiella termer
    terms = {
        "EBIT": "Rörelseresultat före räntor och skatt. Används som ett mått på ett företags operativa vinst.",
        "ROA": "Return on Assets – avkastning på tillgångar. Visar hur effektivt ett företag använder sina tillgångar för att skapa vinst.",
        "Enterprise Value": "Företagsvärde – summan av börsvärde + skulder – kassa. Används för att värdera hela företaget.",
        "P/E-tal": "Price-to-Earnings – aktiekurs delat med vinst per aktie. Vanligt mått på värdering.",
        "Current Ratio": "Omsättningstillgångar delat med kortfristiga skulder. Mäter likviditet.",
        "Bruttomarginal": "Bruttoresultat / omsättning. Visar hur mycket av försäljningen som är kvar efter varukostnad.",
        "Skuldsättningsgrad": "Mäter relationen mellan skulder och eget kapital. Högre värde innebär högre finansiell risk.",
        "Kassaflöde": "De faktiska pengar som strömmar in och ut från verksamheten – ofta viktigare än redovisad vinst.",
        "Kapitalomsättningshastighet": "Omsättning dividerat med totala tillgångar. Visar hur effektivt bolaget använder sina resurser.",
        "Emission": "Utfärdande av nya aktier, vilket späder ut befintligt ägande."
    }

    # Filtrera termer efter sökfras
    filtered_terms = {k: v for k, v in terms.items() if search_query in k.lower() or search_query in v.lower()}

    if filtered_terms:
        for term, definition in filtered_terms.items():
            with st.expander(term):
                st.write(definition)
    else:
        st.info("🔎 Ingen träff. Prova ett annat sökord.")
