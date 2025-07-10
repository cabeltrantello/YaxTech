import axios from 'axios'

const VITE_API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api/v1';
const VITE_API_KEY = import.meta.env.VITE_API_KEY;

if (!VITE_API_KEY) {
  console.error("CRITICAL ERROR: VITE_API_KEY environment variable is not set.");
}

const apiClient = axios.create({
  baseURL: VITE_API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': VITE_API_KEY,
  }
});

export default apiClient;