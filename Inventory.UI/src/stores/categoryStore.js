import { defineStore } from 'pinia';
import axios from 'axios';
import { BACKEND_URL } from '@/config.js';

export const useCategoryStore = defineStore('category', {
  state: () => ({
    categories: [],
    isLoading: false,
    error: null,
  }),
  actions: {
    async fetchCategories() {
      this.isLoading = true;
      this.error = null;
      try {
        const response = await axios.get(`${BACKEND_URL}/categories`);
        this.categories = response.data;
        console.log('Kategorien geladen:', this.categories);
      } catch (err) {
        console.error('Fehler beim Laden der Kategorien:', err);
        this.error = err;
      } finally {
        this.isLoading = false;
      }
    },
  },
});

