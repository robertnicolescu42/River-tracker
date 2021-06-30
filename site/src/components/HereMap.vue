<template>
<l-map style="height: 350px" :zoom="zoom" :center="center">
<l-tile-layer :url="url"></l-tile-layer>
<l-marker v-for="item in data"
        :key="item.id"
        :lat-lng="[item.latitude, item.longitude]"
        :icon="icon">
  <l-popup>Device number {{item.device_id}}.</l-popup>
</l-marker>
<l-icon
          :icon-anchor="staticAnchor"
          class-name="someExtraClass">
<!-- <div class="headline">{{ customText }}</div> -->
</l-icon>
</l-map>
</template>

<script>
import L from 'leaflet';
import {LMap, LTileLayer, LMarker, LIcon, LPopup} from 'vue2-leaflet';


export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon,
    LPopup
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      zoom: this.zoom1,      
      icon: L.icon({
        iconUrl: 'https://image.flaticon.com/icons/png/512/684/684908.png',
        iconSize: [50, 50],
        iconAnchor: [16, 16]
      }),
      staticAnchor: [16, 16],
      //customText: '',
      iconSize: 64
    };
  },
  props: {
   center: Array,
   data: Array,
   zoom1: Number
},
  computed: {
    dynamicSize () {
      return [this.iconSize, this.iconSize * 1.15];
    },
    dynamicAnchor () {
      return [this.iconSize / 2, this.iconSize * 1.15];
    }
  }
}
</script>