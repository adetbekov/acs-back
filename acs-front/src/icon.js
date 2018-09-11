import Vue from 'vue'
import Icon from "vue-awesome/components/Icon"

Vue.component('icon', Icon)

Icon.register({
  'purchased': {
    width: 5,
    height: 5,
    raw: '<svg aria-hidden="true" data-prefix="fas" data-icon="tags" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" class="svg-inline--fa fa-tags fa-w-20" style="font-size: 48px;"><path fill="currentColor" d="M497.941 225.941L286.059 14.059A48 48 0 0 0 252.118 0H48C21.49 0 0 21.49 0 48v204.118a48 48 0 0 0 14.059 33.941l211.882 211.882c18.744 18.745 49.136 18.746 67.882 0l204.118-204.118c18.745-18.745 18.745-49.137 0-67.882zM112 160c-26.51 0-48-21.49-48-48s21.49-48 48-48 48 21.49 48 48-21.49 48-48 48zm513.941 133.823L421.823 497.941c-18.745 18.745-49.137 18.745-67.882 0l-.36-.36L527.64 323.522c16.999-16.999 26.36-39.6 26.36-63.64s-9.362-46.641-26.36-63.64L331.397 0h48.721a48 48 0 0 1 33.941 14.059l211.882 211.882c18.745 18.745 18.745 49.137 0 67.882z" class=""></path></svg>'
  },
  'store': {
    width: 5,
    height: 5,
    raw: '<svg aria-hidden="true" data-prefix="fas" data-icon="shopping-bag" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="svg-inline--fa fa-shopping-bag fa-w-14" style="font-size: 48px;"><path fill="currentColor" d="M352 160v-32C352 57.42 294.579 0 224 0 153.42 0 96 57.42 96 128v32H0v272c0 44.183 35.817 80 80 80h288c44.183 0 80-35.817 80-80V160h-96zm-192-32c0-35.29 28.71-64 64-64s64 28.71 64 64v32H160v-32zm160 120c-13.255 0-24-10.745-24-24s10.745-24 24-24 24 10.745 24 24-10.745 24-24 24zm-192 0c-13.255 0-24-10.745-24-24s10.745-24 24-24 24 10.745 24 24-10.745 24-24 24z" class=""></path></svg>'
  },
  'dashboard': {
    width: 5,
    height: 5,
    raw: '<svg aria-hidden="true" data-prefix="fas" data-icon="tachometer-alt" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="svg-inline--fa fa-tachometer-alt fa-w-18"><path fill="currentColor" d="M75.694 480a48.02 48.02 0 0 1-42.448-25.571C12.023 414.3 0 368.556 0 320 0 160.942 128.942 32 288 32s288 128.942 288 288c0 48.556-12.023 94.3-33.246 134.429A48.018 48.018 0 0 1 500.306 480H75.694zM512 288c-17.673 0-32 14.327-32 32 0 17.673 14.327 32 32 32s32-14.327 32-32c0-17.673-14.327-32-32-32zM288 128c17.673 0 32-14.327 32-32 0-17.673-14.327-32-32-32s-32 14.327-32 32c0 17.673 14.327 32 32 32zM64 288c-17.673 0-32 14.327-32 32 0 17.673 14.327 32 32 32s32-14.327 32-32c0-17.673-14.327-32-32-32zm65.608-158.392c-17.673 0-32 14.327-32 32 0 17.673 14.327 32 32 32s32-14.327 32-32c0-17.673-14.327-32-32-32zm316.784 0c-17.673 0-32 14.327-32 32 0 17.673 14.327 32 32 32s32-14.327 32-32c0-17.673-14.327-32-32-32zm-87.078 31.534c-12.627-4.04-26.133 2.92-30.173 15.544l-45.923 143.511C250.108 322.645 224 350.264 224 384c0 35.346 28.654 64 64 64 35.346 0 64-28.654 64-64 0-19.773-8.971-37.447-23.061-49.187l45.919-143.498c4.039-12.625-2.92-26.133-15.544-30.173z" class=""></path></svg>'
  },
  'home': {
    width: 5,
    height: 5,
    raw: '<svg aria-hidden="true" data-prefix="far" data-icon="home" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="svg-inline--fa fa-home fa-w-18" style="font-size: 48px;"><path fill="currentColor" d="M557.1 240.7L512 203.8V104c0-4.4-3.6-8-8-8h-32c-4.4 0-8 3.6-8 8v60.5L313.4 41.1c-14.7-12.1-36-12.1-50.7 0L18.9 240.7c-3.4 2.8-3.9 7.8-1.1 11.3l20.3 24.8c2.8 3.4 7.8 3.9 11.3 1.1l14.7-12V464c0 8.8 7.2 16 16 16h168c4.4 0 8-3.6 8-8V344h64v128c0 4.4 3.6 8 8 8h168c8.8 0 16-7.2 16-16V265.8l14.7 12c3.4 2.8 8.5 2.3 11.3-1.1l20.3-24.8c2.6-3.4 2.1-8.4-1.3-11.2zM464 432h-96V304c0-4.4-3.6-8-8-8H216c-4.4 0-8 3.6-8 8v128h-96V226.5l170.9-140c2.9-2.4 7.2-2.4 10.1 0l170.9 140V432z" class=""></path></svg>'
  },
  'html5': {
    width: 512,
    height: 512,
    raw: '<path fill="#E34F26" d="M71,460 L30,0 481,0 440,460 255,512"/><path fill="#EF652A" d="M256,472 L405,431 440,37 256,37"/><path fill="#EBEBEB" d="M256,208 L181,208 176,150 256,150 256,94 255,94 114,94 115,109 129,265 256,265zM256,355 L255,355 192,338 188,293 158,293 132,293 139,382 255,414 256,414z"/><path fill="#FFF" d="M255,208 L255,265 325,265 318,338 255,355 255,414 371,382 372,372 385,223 387,208 371,208zM255,94 L255,129 255,150 255,150 392,150 392,150 392,150 393,138 396,109 397,94z"/>'
  },
  'python': {
  	width: 512,
  	height: 512,
  	raw: '<?xml version="1.0" encoding="utf-8"?><!-- Generator: Adobe Illustrator 21.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0) --><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 20 20" enable-background="new 0 0 20 20" xml:space="preserve"><g id="g1894" transform="translate(428.42338,184.2561)"><linearGradient id="path8615_1_" gradientUnits="userSpaceOnUse" x1="-381.6533" y1="-231.5201" x2="-371.7121" y2="-241.4945" gradientTransform="matrix(1 0 0 -1 -44.9375 -413.981)"><stop offset="0" style="stop-color:#387EB8"/><stop offset="1" style="stop-color:#366994"/></linearGradient><path id="path8615" fill="url(#path8615_1_)" d="M-418.5-184.3c-5.1,0-4.8,2.2-4.8,2.2l0,2.3h4.9v0.7h-6.8c0,0-3.3-0.4-3.3,4.8s2.9,5,2.9,5h1.7v-2.4c0,0-0.1-2.9,2.8-2.9s4.8,0,4.8,0s2.7,0,2.7-2.6c0-2.7,0-4.4,0-4.4S-413.2-184.3-418.5-184.3z M-421.2-182.7c0.5,0,0.9,0.4,0.9,0.9s-0.4,0.9-0.9,0.9c-0.5,0-0.9-0.4-0.9-0.9S-421.7-182.7-421.2-182.7z"/><linearGradient id="path8620_1_" gradientUnits="userSpaceOnUse" x1="-375.54" y1="-237.8698" x2="-364.8632" y2="-248.0988" gradientTransform="matrix(1 0 0 -1 -44.9375 -413.981)"><stop offset="0" style="stop-color:#FFE052"/><stop offset="1" style="stop-color:#FFC331"/></linearGradient><path id="path8620" fill="url(#path8620_1_)" d="M-418.4-164.3c5.1,0,4.8-2.2,4.8-2.2l0-2.3h-4.9v-0.7h6.8c0,0,3.3,0.4,3.3-4.8s-2.9-5-2.9-5h-1.7v2.4c0,0,0.1,2.9-2.8,2.9s-4.8,0-4.8,0s-2.7,0-2.7,2.6c0,2.7,0,4.4,0,4.4S-423.7-164.3-418.4-164.3z M-415.7-165.8c-0.5,0-0.9-0.4-0.9-0.9s0.4-0.9,0.9-0.9c0.5,0,0.9,0.4,0.9,0.9S-415.2-165.8-415.7-165.8z"/></g></svg>'
  },
  'vue': {
    width: 512,
    height: 512,
    raw: '<?xml version="1.0" encoding="utf-8"?><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 400 346" enable-background="new 0 0 400 346" xml:space="preserve"><g id="g10" transform="matrix(1.3333333,0,0,-1.3333333,0,400)"><g id="g12" transform="translate(178.0626,235.0086)"><path id="path14" fill="#4DBA87" d="M6.6,65L-28.1,5l-34.6,60h-115.4l150-259.8L121.9,65H6.6z"/></g><g id="g16" transform="translate(178.0626,235.0086)"><path id="path18" fill="#435466" d="M6.6,65L-28.1,5l-34.6,60h-55.4l90-155.9L61.9,65H6.6z"/></g></svg>'
  },
})