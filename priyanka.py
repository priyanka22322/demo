import streamlit as st

def rectangular_moment_of_inertia(b, h):
    return (1/12) * b * (h**3)

def circular_moment_of_inertia(r):
    return (1/4) * 3.1416 * (r**4)

def moment_of_inertia(shape, *args):
    if shape == 'Rectangle':
        return rectangular_moment_of_inertia(*args)
    elif shape == 'Circle':
        return circular_moment_of_inertia(*args)

def main():
    st.title("Moment of Inertia Calculator")
    st.sidebar.header("Select Shape")

    shape = st.sidebar.radio("Choose a shape", ('Rectangle', 'Circle'))

    st.sidebar.header("Input Parameters")

    if shape == 'Rectangle':
        b = st.sidebar.number_input("Enter the base (b)", min_value=0.0)
        h = st.sidebar.number_input("Enter the height (h)", min_value=0.0)
        result = moment_of_inertia(shape, b, h)
    elif shape == 'Circle':
        r = st.sidebar.number_input("Enter the radius (r)", min_value=0.0)
        result = moment_of_inertia(shape, r)

    st.subheader(f"{shape} Moment of Inertia:")
    st.write(result)
st.write("The moment of inertia is defined as the quantity expressed by the body resisting angular acceleration, which is the sum of the product of the mass of every particle with its square of the distance from the axis of rotation.")
if __name__ == "__main__":
    main()