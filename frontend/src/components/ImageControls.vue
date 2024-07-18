<template>
    <div class="col">
        <control-button classe="nf-md-flip_vertical" @click="processImage('flip_y')">
            Espelhar vertical
        </control-button>
    </div>
    <div class="col">
        <control-button classe="nf-md-flip_horizontal" @click="processImage('flip_x')">
            Espelhar horizontal
        </control-button>
    </div>
    <div class="col">
        <control-button classe="nf nf-fa-rotate_left" @click="processImage('rotate_l')">
            Girar à esquerda
        </control-button>
    </div>
    <div class="col">
        <control-button classe="nf-fa-rotate_right" @click="processImage('rotate_r')">
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