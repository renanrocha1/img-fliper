<template>
    <div id="file-input" class="d-flex justify-content-center align-items-center border border-5 rounded-5 border-primary-subtle p-5" @dragover.prevent @dragenter.prevent @drop="onDrop">
        <label class="btn btn-link" for="file">Arraste sua imagem aqui ou escolha um arquivo</label>
        <input ref="input" class="d-none" type="file" name="file" id="file" @change="previewChange">
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
const input = ref<HTMLInputElement>()
const emit = defineEmits(['previewChange'])

function previewChange(event: Event) {
    const input = event.target as HTMLInputElement
    postFileEvt(input);
}

function postFileEvt(input: HTMLInputElement) {
    if (input.files) {
        const reader = new FileReader();
        reader.onload = e => emit('previewChange', e.target?.result, input.files![0]);
        reader.readAsDataURL(input.files[0]);
    }
}

function onDrop(event: DragEvent) {
    const dt = new DataTransfer()
    dt.items.add(event.dataTransfer!.files[0])
    input.value!.files = dt.files
    postFileEvt(input.value!)
    event.preventDefault()
}
</script>

<style scoped>
#file-input {
    min-height: 150px;
    border-style: dashed !important;
}
</style>