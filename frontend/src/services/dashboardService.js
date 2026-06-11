// src/services/dashboardService.js

import api from "./api";

export const getDashboardStats = async () => {
  try {
    const response = await api.get("/stats");
    return response.data;
  } catch (error) {
    console.error("Error fetching dashboard stats:", error);
    throw error;
  }
};