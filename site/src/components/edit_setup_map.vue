<template>
  <div>
    <l-map
      style="height: 428px"
      :zoom="zoom"
      :center="this.center"
      @click="addMarker"
    >
      <l-tile-layer :url="url"></l-tile-layer>
      <l-marker
        v-for="item in markers"
        :key="item"
        :lat-lng="item"
        :icon="icon"
      >
      </l-marker>
      <l-icon :icon-anchor="staticAnchor" class-name="someExtraClass"> </l-icon>
    </l-map>
    <div>
      <v-container>

      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field v-model="low_bound" :rules="rules.a" label="Low bound" :placeholder="data.low_bound" required></v-text-field>
        <v-text-field v-model="high_bound" :rules="rules.a" label="high bound" :placeholder="data.high_bound" required></v-text-field>
        <v-text-field
          v-model="river_height"
          label="River height"
          :placeholder="data.river_height"
          :rules="rules.a"
          required
        ></v-text-field>
        <v-text-field
          v-model="river_difference"
          label="River diffrence"
          :placeholder="data.river_difference"
          :rules="rules.a"
          required
        ></v-text-field>

        <v-btn
          color="success"
          class="mr-4"
          @click="UpdateDevice"
        >
          Submit
        </v-btn>
      </v-form>
      </v-container>
    </div>

    <!-- {{markers}} -->
  </div>
</template>

<script>
import { db } from "../firebase/db.js";
import L from "leaflet";
import { LMap, LTileLayer, LMarker, LIcon } from "vue2-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon,
  },
  props: {
    data: Object,
    add: Boolean
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      zoom: 13,
      icon: L.icon({
        iconUrl: "https://image.flaticon.com/icons/png/512/684/684908.png",
        iconSize: [50, 50],
        iconAnchor: [16, 16],
      }),
      clicked: false,
      markers: [],
      center: [44.848928713917395, 24.892791371311404],
      staticAnchor: [16, 16],
      iconSize: 64,
      low_bound:0,
      high_bound:0,
      river_height:0,
      river_difference:0,
      data1:{},
       rules: {
          a: [
            val => isNaN(val) == false  || `Not a number`,
          ],
        },
    };
  },
  mounted: function () {
    this.low_bound = this.data.low_bound
    this.high_bound = this.data.high_bound
    this.river_height = this.data.river_height
    this.river_difference = this.data.river_difference
    this.markers.push({"lat":this.data.latitude, "lng":this.data.longitude});
    this.center = [this.data.latitude, this.data.longitude];
    setTimeout(function () {
      window.dispatchEvent(new Event("resize"));
    }, 200);
  },
  watch: {
    data: function (val) {
    this.low_bound = val.low_bound
    this.high_bound = val.high_bound
    this.river_height = val.river_height
    this.river_difference = val.river_difference
    this.markers=[]
    this.markers.push({"lat":val.latitude, "lng":val.longitude});
    this.center = [val.latitude, val.longitude];
    },
  },
  firestore: {
    data1: db.collection("setup_data").orderBy("device_id", "asc"),
  },
  methods: {
    UpdateDevice(){
      if(this.add == false){

        db.collection("setup_data")
          .doc(this.data.id)
          .update({
            low_bound: Number(this.low_bound),
            high_bound: Number(this.high_bound),
            river_difference: Number(this.river_difference),
            river_height: Number(this.river_height),
            latitude: this.markers[0].lat,
            longitude: this.markers[0].lng,
          });
    }else{ 
      db.collection("setup_data")
          .add({
            device_id: this.data1.slice(-1)[0].device_id + 1,
            low_bound: Number(this.low_bound),
            high_bound: Number(this.high_bound),
            river_difference: Number(this.river_difference),
            river_height: Number(this.river_height),
            latitude: this.markers[0].lat,
            longitude: this.markers[0].lng,
          });
    }
    },
    addMarker(event) {
      this.markers=[]
        this.markers.push(event.latlng);
        this.clicked = true;

    },
  },
  computed: {
    dynamicSize() {
      return [this.iconSize, this.iconSize * 1.15];
    },
    dynamicAnchor() {
      return [this.iconSize / 2, this.iconSize * 1.15];
    },
  },
};
</script>