<template>
<l-map style="height: 350px" :zoom="zoom" :center="center">
<l-tile-layer :url="url"></l-tile-layer>
<l-marker :lat-lng="[47.413220, -1.219482]" > </l-marker>
<l-marker
        :lat-lng="[47.413220, -1.209482]"
        :icon="icon" > </l-marker>
<l-marker :lat-lng="[47.413220, -1.199482]">
<l-icon
          :icon-size="dynamicSize"
          :icon-anchor="dynamicAnchor"
          icon-url="static/images/baseball-marker.png" >
</l-icon>
</l-marker>
<l-marker :lat-lng="[47.413220, -1.189482]">
<l-icon
          :icon-anchor="staticAnchor"
          class-name="someExtraClass">
<div class="headline">{{ customText }}</div>
<img src="/images/layers.png">
</l-icon>
</l-marker>
</l-map>
</template>

<script>
import L from 'leaflet';
import {LMap, LTileLayer, LMarker, LIcon} from 'vue2-leaflet';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      zoom: 13,
      center: [47.413220, -1.219482],
      icon: L.icon({
        iconUrl: 'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/slideshows/is_my_cat_normal_slideshow/1800x1200_is_my_cat_normal_slideshow.jpg',
        iconSize: [100, 100],
        iconAnchor: [16, 37]
      }),
      staticAnchor: [16, 37],
      customText: 'Foobar',
      iconSize: 64
    };
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