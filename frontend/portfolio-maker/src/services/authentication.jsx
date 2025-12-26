import axios from "axios";
const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export const register = async (userData) => {
  try {
    const response = await axios.post(
      `${API_URL}/accounts/register/`,
      userData
    );
    // Sav token in localStorage
    localStorage.setItem("token", response.data.token);
    return response.data;
  } catch (error) {
    throw error.response?.data || error;
  }
};

export const login = async (credentials) => {
  try {
    const response = await axios.post(
      `${API_URL}/accounts/login/`,
      credentials
    ); // save the token in localStorage
    localStorage.setItem("token", response.data.token);
    return response.data;
  } catch (error) {
    throw error.response?.data || error;
  }
};
