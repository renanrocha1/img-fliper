<template>
    <div class="col d-flex justify-content-center">
        <control-button classe="nf-md-flip_vertical h-100" @click="processImage('flip_y')">
            Espelhar vertical
        </control-button>
    </div>
    <div class="col d-flex justify-content-center">
        <control-button classe="nf-md-flip_horizontal h-100" @click="processImage('flip_x')">
            Espelhar horizontal
        </control-button>
    </div>
    <div class="col d-flex justify-content-center">
        <control-button classe="nf nf-fa-rotate_left h-100" @click="processImage('rotate_l')">
            Girar à esquerda
        </control-button>
    </div>
    <div class="col d-flex justify-content-center">
        <control-button classe="nf-fa-rotate_right h-100" @click="processImage('rotate_r')">
            Girar à direita
        </control-button>
    </div>
</template>

<script setup lang="ts">
import ControlButton from './ControlButton.vue'
defineProps<{
    processImage: Function
}>()
</script>