import streamlit as st

# =====================================================
# PAGE SETTINGS
# =====================================================
st.set_page_config(page_title="Power Electronics Toolkit", layout="wide")

st.title("⚡ Power Electronics Toolkit")
st.markdown("All daily power electronics calculations in one place")

# =====================================================
# SIDEBAR
# =====================================================
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

# =====================================================
# 1. OHM LAW
# =====================================================
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

        st.success(f"V = {V:.3f} V")
        st.success(f"I = {I:.3f} A")
        st.success(f"R = {R:.3f} Ω")
        st.success(f"Power = {P:.3f} W")


# =====================================================
# 2. VOLTAGE DIVIDER
# =====================================================
elif menu == "Voltage Divider":

    st.header("🔹 Voltage Divider")

    Vin = st.number_input("Vin (V)", value=12.0)
    R1 = st.number_input("R1 (Ω)", value=10000.0)
    R2 = st.number_input("R2 (Ω)", value=10000.0)

    if st.button("Calculate"):
        Vout = Vin * (R2 / (R1 + R2))
        st.success(f"Vout = {Vout:.3f} V")


# =====================================================
# 3. BATTERY RUNTIME (FIXED)
# =====================================================
elif menu == "Battery Runtime":

    st.header("🔋 Battery Runtime Calculator")

    Ah = st.number_input("Capacity (Ah)", value=2.6)
    Vavg = st.number_input("Average Voltage (V)", value=7.4)
    load = st.number_input("Load Power (W)", value=5.0)
    standby = st.number_input("Standby Power (W)", value=0.2)
    eff = st.slider("Efficiency (%)", 50, 100, 90)

    if st.button("Calculate"):

        total_power = load + standby

        if total_power == 0:
            st.error("Power cannot be 0")
        else:
            energy = Ah * Vavg
            runtime = (energy * (eff / 100)) / total_power
            runtime_real = runtime * 0.85

            st.success(f"Energy = {energy:.2f} Wh")
            st.success(f"Ideal Runtime = {runtime:.2f} hours")
            st.info(f"Realistic Runtime ≈ {runtime_real:.2f} hours")


# =====================================================
# 4. BATTERY PACK BUILDER
# =====================================================
elif menu == "Battery Pack Builder":

    st.header("🔋 Battery Pack Builder")

    S = st.number_input("Series Cells", value=2)
    P = st.number_input("Parallel Cells", value=2)
    cellV = st.number_input("Cell Voltage (V)", value=3.7)
    cellAh = st.number_input("Cell Capacity (Ah)", value=2.6)

    if st.button("Calculate"):

        packV = S * cellV
        packAh = P * cellAh
        energy = packV * packAh

        st.success(f"Pack Voltage = {packV:.2f} V")
        st.success(f"Pack Capacity = {packAh:.2f} Ah")
        st.success(f"Energy = {energy:.2f} Wh")


# =====================================================
# 5. BOOST
# =====================================================
elif menu == "Boost Converter":

    st.header("⚡ Boost Converter")

    Vin = st.number_input("Input Voltage", value=5.0)
    Vout = st.number_input("Output Voltage", value=12.0)
    Iout = st.number_input("Output Current (A)", value=1.0)
    eff = st.slider("Efficiency %", 50, 100, 90)

    if st.button("Calculate"):

        D = 1 - (Vin / Vout)
        Pin = (Vout * Iout) / (eff / 100)
        Iin = Pin / Vin

        st.success(f"Duty Cycle = {D*100:.2f}%")
        st.success(f"Input Current = {Iin:.2f} A")


# =====================================================
# 6. BUCK
# =====================================================
elif menu == "Buck Converter":

    st.header("⚡ Buck Converter")

    Vin = st.number_input("Vin (V)", value=12.0)
    Vout = st.number_input("Vout (V)", value=5.0)
    Iout = st.number_input("Iout (A)", value=1.0)
    eff = st.slider("Efficiency %", 50, 100, 95)

    if st.button("Calculate"):

        D = Vout / Vin
        Pin = (Vout * Iout) / (eff / 100)
        Iin = Pin / Vin

        st.success(f"Duty = {D*100:.2f}%")
        st.success(f"Input Current = {Iin:.2f} A")


# =====================================================
# 7. EFFICIENCY
# =====================================================
elif menu == "Efficiency & Loss":

    st.header("⚡ Efficiency Calculator")

    Pin = st.number_input("Input Power (W)", value=10.0)
    Pout = st.number_input("Output Power (W)", value=9.0)

    if st.button("Calculate"):

        eff = (Pout / Pin) * 100
        loss = Pin - Pout

        st.success(f"Efficiency = {eff:.2f}%")
        st.success(f"Loss = {loss:.2f} W")


# =====================================================
# 8. ADC DIVIDER
# =====================================================
elif menu == "ADC Divider (STM)":

    st.header("📐 ADC Divider")

    Vin = st.number_input("Max Input Voltage", value=12.0)
    Vref = st.number_input("ADC Reference", value=3.3)
    R2 = st.number_input("Bottom Resistor (kΩ)", value=10.0)

    if st.button("Calculate"):
        R1 = (Vin / Vref - 1) * R2
        st.success(f"Top Resistor ≈ {R1:.2f} kΩ")


# =====================================================
# 9. SENSE RESISTOR
# =====================================================
elif menu == "Sense Resistor":

    st.header("🔧 Current Sense Resistor")

    I = st.number_input("Current (A)", value=1.0)
    Vsense = st.number_input("Sense Voltage (V)", value=0.1)

    if st.button("Calculate"):
        R = Vsense / I
        P = I * I * R

        st.success(f"R = {R:.4f} Ω")
        st.success(f"Power = {P:.2f} W")


# =====================================================
# 10. STANDBY
# =====================================================
elif menu == "Standby Drain":

    st.header("🔋 Standby Drain")

    Ah = st.number_input("Battery Ah", value=2.6)
    V = st.number_input("Voltage", value=7.4)
    I = st.number_input("Standby Current (A)", value=0.01)

    if st.button("Calculate"):

        power = V * I
        hours = (Ah * V) / power

        st.success(f"Standby power = {power:.3f} W")
        st.success(f"Battery lasts ≈ {hours:.1f} hours")
