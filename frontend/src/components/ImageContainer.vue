<template>
    <div class="d-flex justify-content-center align-items-center flex-column">
        <slot></slot>
        <div class="w-100 h-100 border border-2 rounded-5 p-4">
            <img :src="src" alt="image">
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";
defineProps(['src'])
</script>

<style scoped>
img {
    max-width: 95%;
}
</style>