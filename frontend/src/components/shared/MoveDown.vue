<template>
    <div class="movedown">
      <slot></slot>
    </div>
</template>

<script>
export default {
  name: 'MoveDown'
}
</script>

<style scoped>
.movedown {
  position: relative;
  cursor: pointer;
  animation:bmmove 2s infinite;
  -moz-animation:bmmove 2s infinite; /* Firefox */
  -webkit-animation:bmmove 2s infinite; /* Safari and Chrome */
}
@keyframes bmmove {
0% {top: 0px;}
50% {top: 10px;}
100% {top: 0px;}

}
@-moz-keyframes bmmove {
0% {top: 0px;}
50% {top: 10px;}
}
@-webkit-keyframes bmmove {
0% {top: 0px;}
50% {top: 10px;}
}
</style>
