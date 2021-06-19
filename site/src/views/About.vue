<template>
<div>
<l-map style="height: 500px" :zoom="zoom" :center="this.center" @click="addMarker">
<l-tile-layer :url="url"></l-tile-layer>
<l-marker 
        v-for="item in markers"
        :key="item"
        :lat-lng="item"
        :icon="icon">
  <!-- <l-popup>Device number {{item.device_id}}.</l-popup> -->
</l-marker>
<l-icon
          :icon-anchor="staticAnchor"
          class-name="someExtraClass">
<!-- <div class="headline">{{ customText }}</div> -->
</l-icon>
</l-map>
{{markers}}

</div>
</template>

<script>
import L from 'leaflet';
import {LMap, LTileLayer, LMarker, LIcon} from 'vue2-leaflet';


export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon,
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      zoom: 13,      
      icon: L.icon({
        iconUrl: 'https://image.flaticon.com/icons/png/512/684/684908.png',
        iconSize: [50, 50],
        iconAnchor: [16, 16]
      }),
      clicked: false,
      markers: [
      ],
      center: [44.848928713917395, 24.892791371311404],
      staticAnchor: [16, 16],
      //customText: '',
      iconSize: 64
    };
  },
  methods:{
    addMarker(event) {
      if(this.markers.length == 0){
        this.markers.push(event.latlng);
        this.clicked = true;
      }else{
        this.markers.splice(event, 1);
        this.markers.push(event.latlng);
      }

    },
  },
  props: {

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