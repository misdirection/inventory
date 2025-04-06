<template>
  <v-container>
    <v-card>
      <v-card-title>Kategorien</v-card-title>
      <v-card-text>
        <v-progress-linear v-if="categoryStore.isLoading" indeterminate color="primary"></v-progress-linear>

        <v-alert type="error" v-if="categoryStore.error">
          Fehler beim Laden der Kategorien.
        </v-alert>

        <v-list v-else>
          <v-list-item v-for="category in categoryStore.categories" :key="category.id">
            <v-list-item-content>
              <v-list-item-title>{{ category.name }}</v-list-item-title>
              <v-list-item-subtitle>{{ category.description }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCategoryStore } from '@/stores/categoryStore';

const categoryStore = useCategoryStore();

onMounted(() => {
  categoryStore.fetchCategories();
});
</script>

<style scoped></style>
