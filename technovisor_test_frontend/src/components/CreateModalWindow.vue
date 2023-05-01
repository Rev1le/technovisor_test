<template>
    <transition name="v-dialog">
    <div class="dialog" @click.stop="hideDialog" v-if="show">
        <div @click.stop class="dialog-content">
            <slot>

            </slot>
        </div>
    </div>
    </transition>

    <transition name="back">
    <div @click.stop="hideDialog" v-if="show" class="back">

    </div>
  </transition>
</template>

<script>


export default{
    name: "CreateModalWindow",
    props:{
        show : {
            type : Boolean,
            default: false
        }
    },
    methods:{
        hideDialog(){
            this.$emit('update:show', false);
        }

    }
}
</script>

<style>

.dialog{
    z-index: 10;
    top:0;
    bottom: 0;
    right: 0;
    left: 0;
    background: none;
    position: fixed;
    display: flex;
}
.dialog-content{
    margin: auto;
    border-radius: 12px;
    padding: 15px;
    min-height: 50px;
    min-width: 300px;
    max-width: 40%;
    background: #0ea2bd;
}

.back-enter-active,
.back-leave-active {
  transition: opacity 0.8s;
}

.back-enter-from,
.back-leave-to {
  opacity: 0;
}


.back{
  position: fixed;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  width: 100%;
  top: 0;
  left: 0;
  z-index: 9;
  transition: 0.3s ease-in-out ;
}
.v-dialog-enter-active,
.v-dialog-leave-active {
  transition: all 0.4s;
}

.v-dialog-enter-from {
  opacity: 0;

  transform: translate(-100%, 0px);

}

.v-dialog-leave-to {
  opacity: 0;
  
  transform: translate(0px, -100%);
}
</style>