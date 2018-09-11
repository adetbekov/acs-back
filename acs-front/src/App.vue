<template>
  <div id="app" class="Site d-flex flex-column flex-nowrap">
      <router-view class="Site-content"></router-view>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  export default {
    name: 'app',
    components: {
      Navbar
    }
  }
</script>

<style>
  @font-face {
    font-family: 'BebasNeue';
    src: url('./assets/fonts/Bebas_Neue/BebasNeue_Regular.otf');
  }
  @font-face {
    font-family: 'BebasNeue';
    src: url('./assets/fonts/Bebas_Neue/BebasNeue_Bold.otf');
    font-weight: bold;
  }
  @font-face {
    font-family: 'BebasNeue';
    src: url('./assets/fonts/Bebas_Neue/BebasNeue_Book.otf');
    font-weight: 300;
  }
  @font-face {
    font-family: 'BebasNeue';
    src: url('./assets/fonts/Bebas_Neue/BebasNeue_Light.otf');
    font-weight: 200;
  }
  @font-face {
    font-family: 'BebasNeue';
    src: url('./assets/fonts/Bebas_Neue/BebasNeue_Thin.otf');
    font-weight: 100;
  }

  @font-face {
    font-family: 'Lobster';
    src: url('./assets/fonts/Lobster/Lobster-Regular.ttf');
  }
  @font-face {
    font-family: 'Amatic SC';
    src: url('./assets/fonts/Amatic_SC/AmaticSC-Regular.ttf');
  }
  @font-face {
    font-family: 'Amatic SC';
    src: url('./assets/fonts/Amatic_SC/AmaticSC-Bold.ttf');
    font-weight: bold;
  }
  @font-face {
    font-family: 'Playfair Display';
    src: url('./assets/fonts/Playfair_Display/PlayfairDisplay-Regular.ttf');
  }
  @font-face {
    font-family: 'Playfair Display';
    src: url('./assets/fonts/Playfair_Display/PlayfairDisplay-Bold.ttf');
    font-weight: bold;
  }
  body,html {
    background-color: white;
    min-width: 100%;
    min-height: 100%;
    padding: 0;
    margin: 0;
  }
  body, #app {
    min-height: 100vh;
  }
  #app {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    height: 100%;
  }
  .fw-100 {
    font-weight: 100;
  }
  .fw-300 {
    font-weight: 300;
  }
  .fw-500 {
    font-weight: 500;
  }
  .header {
    padding-top: 20px;
    min-height: 60px;
  }
  /*.Site {
    display: flex;
    min-height: 100vh ;
    flex-direction: column;
  }

  .Site-content {
    flex: 1;
    max-width: 100%;
  }*/
  .text-gray {
    color: #7e7f81;
  }
</style>
