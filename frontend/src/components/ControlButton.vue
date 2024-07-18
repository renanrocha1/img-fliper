<template>
    <button class="btn btn-secondary fs-5">
        <i class="nf fs-2" :class="classe"></i><br>
        <slot></slot>
    </button>
</template>

<script setup lang="ts">
defineProps(['classe'])
</script>