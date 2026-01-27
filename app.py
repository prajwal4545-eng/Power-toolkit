import streamlit as st

st.set_page_config(page_title="Power Electronics Calculator", layout="wide")

st.title("⚡Power Electronics Toolkit")
st.markdown("All daily power electronics calculations in one place")

# ==========================================
# SIDEBAR MENU
# ==========================================

menu = st.sidebar.radio(
    "Select Calculator",
    [
        "Ohm & Power",
        "Voltage Divider",
        "Battery Runtime",
        "Battery Pack Builder",
        "Boost Converter",
        "Buck Converter",
        "Efficiency & Loss",
        "ADC Divider (STM)",
        "Sense Resistor",
        "Standby Drain"
    ]
)


# ==========================================
# 1. OHM + POWER
# ==========================================
if menu == "Ohm & Power":

    st.header("🔹 Ohm & Power Calculator")

    V = st.number_input("Voltage (V)", value=0.0)
    I = st.number_input("Current (A)", value=0.0)
    R = st.number_input("Resistance (Ω)", value=0.0)

    if st.button("Solve"):
        if V == 0 and I and R:
            V = I * R
        elif I == 0 and V and R:
            I = V / R
        elif R == 0 and V and I:
            R = V / I

        P = V * I
        st.success(f"V={V:.3f} V   I={I:.3f} A   R={R:.3f} Ω   Power={P:.3f} W")


# ==========================================
# 2. VOLTAGE DIVIDER
# ==========================================
elif menu == "Voltage Divider":

    st.header("🔹 Voltage Divider")

    Vin = st.number_input("Vin (V)")
    R1 = st.number_input("R1 (Ω)")
    R2 = st.number_input("R2 (Ω)")

    if st.button("Calculate"):
        if R1 and R2:
            Vout = Vin * (R2 / (R1 + R2))
            st.success(f"Vout = {Vout:.3f} V")


# ==========================================
# 3. BATTERY RUNTIME
# ==========================================
elif menu == "Battery Runtime":

    st.header("🔋 Battery Runtime Calculator")

    Ah = st.number_input("Capacity (Ah)")
    Vavg = st.number_input("Average Voltage (V)", value=7.2)
    load = st.number_input("Load Power (W)")
    eff = st.slider("Efficiency (%)", 50, 100, 90)
    standby = st.number_input("Standby Power (W)", value=0.1)

    if st.button("Calculate"):
        energy = Ah * Vavg
        total_power = load + standby
        runtime = energy / (total_power / (eff/100))

        st.success(f"Energy = {energy:.2f} Wh")
        st.success(f"Runtime ≈ {runtime:.2f} hours")


# ==========================================
# 4. BATTERY PACK
# ==========================================
elif menu == "Battery Pack Builder":

    st.header("🔋 Battery Pack Builder")

    S = st.number_input("Series Cells")
    P = st.number_input("Parallel Cells")
    cellV = st.number_input("Cell Voltage", value=3.7)
    cellAh = st.number_input("Cell Capacity (Ah)")

    if st.button("Calculate"):
        packV = S * cellV
        packAh = P * cellAh
        energy = packV * packAh

        st.success(f"Pack Voltage = {packV:.2f} V")
        st.success(f"Pack Capacity = {packAh:.2f} Ah")
        st.success(f"Energy = {energy:.2f} Wh")


# ==========================================
# 5. BOOST
# ==========================================
elif menu == "Boost Converter":

    st.header("⚡ Boost Converter")

    Vin = st.number_input("Input Voltage")
    Vout = st.number_input("Output Voltage")
    Iout = st.number_input("Output Current")
    eff = st.slider("Efficiency %", 50, 100, 90)

    if st.button("Calculate"):
        D = 1 - (Vin / Vout)
        Pin = (Vout * Iout) / (eff/100)
        Iin = Pin / Vin

        st.success(f"Duty Cycle = {D*100:.2f}%")
        st.success(f"Input Current = {Iin:.2f} A")


# ==========================================
# 6. BUCK
# ==========================================
elif menu == "Buck Converter":

    st.header("⚡ Buck Converter")

    Vin = st.number_input("Vin")
    Vout = st.number_input("Vout")
    Iout = st.number_input("Iout")
    eff = st.slider("Efficiency %", 50, 100, 95)

    if st.button("Calculate"):
        D = Vout / Vin
        Pin = (Vout * Iout) / (eff/100)
        Iin = Pin / Vin

        st.success(f"Duty = {D*100:.2f}%")
        st.success(f"Input Current = {Iin:.2f} A")


# ==========================================
# 7. EFFICIENCY
# ==========================================
elif menu == "Efficiency & Loss":

    st.header("⚡ Efficiency Calculator")

    Pin = st.number_input("Input Power (W)")
    Pout = st.number_input("Output Power (W)")

    if st.button("Calculate"):
        eff = (Pout / Pin) * 100
        loss = Pin - Pout

        st.success(f"Efficiency = {eff:.2f}%")
        st.success(f"Loss = {loss:.2f} W")


# ==========================================
# 8. ADC DIVIDER
# ==========================================
elif menu == "ADC Divider (STM)":

    st.header("📐 ADC Divider")

    Vin = st.number_input("Max Input Voltage")
    Vref = st.number_input("ADC Reference", value=3.3)
    R2 = st.number_input("Bottom Resistor (kΩ)")

    if st.button("Calculate"):
        R1 = (Vin/Vref - 1) * R2
        st.success(f"Top Resistor ≈ {R1:.2f} kΩ")


# ==========================================
# 9. SENSE RESISTOR
# ==========================================
elif menu == "Sense Resistor":

    st.header("🔧 Current Sense Resistor")

    I = st.number_input("Current (A)")
    Vsense = st.number_input("Sense Voltage (V)", value=0.1)

    if st.button("Calculate"):
        R = Vsense / I
        P = I*I*R

        st.success(f"R = {R:.4f} Ω")
        st.success(f"Power = {P:.2f} W")


# ==========================================
# 10. STANDBY
# ==========================================
elif menu == "Standby Drain":

    st.header("🔋 Standby Drain")

    Ah = st.number_input("Battery Ah")
    V = st.number_input("Voltage")
    I = st.number_input("Standby Current (A)")

    if st.button("Calculate"):
        energy = Ah * V
        power = V * I
        hours = energy / power

        st.success(f"Standby power = {power:.3f} W")
        st.success(f"Battery lasts ≈ {hours:.1f} hours")

