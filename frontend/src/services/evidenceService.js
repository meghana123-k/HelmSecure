// services/evidenceService.js

import api from "./api";

export const fetchEvidence = async() => {
    try {
        const response = await api.get("/evidence");
        return response.data;   
    } catch (error) {
        console.error("Error fetching evidence info:", error);
        throw error;
    } 
}