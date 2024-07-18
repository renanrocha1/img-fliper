<script setup lang="ts">
import { ref } from "vue";
import axios from 'axios'
import ImageContainer from "./components/ImageContainer.vue";
import FileInput from "./components/FileInput.vue";
import ImageControls from "./components/ImageControls.vue";

const preview = ref<string>()
const result = ref<string>()
const srcFile = ref<File>()
const destFile = ref<File>()

function previewImage(previewSrc: string, file: File) {
  preview.value = previewSrc
  result.value = previewSrc
  srcFile.value = file
  destFile.value = file
}

async function processImage(direction: string) {
  if (destFile.value) {
    const formdata = new FormData()
    formdata.append('file', destFile.value)
    const response = await axios.post(`http://localhost:8000/image/${direction}`, formdata, {responseType: 'blob'})
    destFile.value = new File([response.data], destFile.value.name)
    result.value = URL.createObjectURL(response.data)
  }
}
</script>

<template>
  
  <div class="d-flex flex-column content">
    <header>
      <nav class="navbar bg-body-tertiary">
        <div class="container-fluid">
          <h1 class="navbar-brand mb-0 h1 text-center">Image Flip</h1>
        </div>
      </nav>
    </header>
    <div class="container-fluid flex-grow-1 row align-items-center justify-content-center ">
      <template v-if="preview">
        <div class="row d-flex">
          <image-container class="col-6" :src="preview">
            <h3 class="mb-4">Original</h3>
          </image-container>
          <image-container class="col-6" :src="result">
            <h3 class="mb-4">Alterada</h3>
          </image-container>
        </div>
        <div class="row">
          <image-controls :processImage="processImage"/>
        </div>
      </template>
      <template v-else>
        <div class="col d-flex justify-content-center">
          <file-input @preview-change="previewImage"/>
        </div>
      </template>
    </div>

  </div>
</template>

<style scoped>
@import "https://www.nerdfonts.com/assets/css/webfont.css";
.content {
  min-height: 100vh;
}
</style>
