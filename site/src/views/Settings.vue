<template>
  <v-container>
    <v-dialog v-model="dialogShow" max-width="900px" max-height="800" style="z-index:1000" >
      <v-card>
        <v-card-title>
          <span class="headline">Location</span>
        </v-card-title>


        <mapSetup />


        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialogShow = false">
            Exit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Are you sure you want to delete this item?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteItemConfirm"
            >OK</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <HereMap style="margin-bottom: 3em" :center="center" :data="data" />
    <v-simple-table dark>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Device ID</th>
            <th class="text-left">Low bound</th>
            <th class="text-left">High bound</th>
            <th class="text-left">River height</th>
            <th class="text-left">River difference</th>

            <!-- <th class="text-left">
            Location
          </th> -->
            <th class="">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in data" :key="item.device_id">
            <td>{{ item.device_id }}</td>
            <td>{{ item.low_bound }}</td>
            <td>{{ item.high_bound }}</td>
            <td>{{ item.river_height }}</td>
            <td>{{ item.river_difference }}</td>
            <!-- <td>{{ item.location }}</td> -->
            <td>
              <v-icon small class="mr-2" @click="ShowItem(item)">
                mdi-map-marker
              </v-icon>
              <v-icon small class="mr-2" @click="editItem(item)">
                mdi-pencil
              </v-icon>
              <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <!-- <pre>{{data[0]}}</pre> -->
  </v-container>
</template>

<script>
import { db } from "../firebase/db.js";
import HereMap from '../components/HereMap'
import MapSetup from '../components/edit_setup_map'
export default {
  components: {
    HereMap,
    MapSetup
  },
  data() {
    return {
      map_link:
        "https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=44.868998803301714,%2024.87540205443056+(My%20Business%20Name)&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed",
      data: [],
      dialogShow: false,
      dialog: false,
      dialogDelete: false,
      editedIndex: -1,
      editedItem: {},
      center:[0,0]
    };
  },
  computed:{
    longitude(){
      return this.data.map((x => x.longitude));
    },
     
    latitude(){
      return this.data.map((x => x.latitude));
    },
  },
  watch: {
    data: function(val){
      this.center= [val[0].latitude, val[0].longitude]
    },
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  firestore: {
    data: db.collection("setup_data").orderBy("device_id", "asc"),
  },
  methods: {
    deleteItem(item) {
      this.center = [item.latitude, item.longitude]
      this.editedIndex = item;
      this.dialogDelete = true;
    },
    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    deleteItemConfirm() {
      let data_id = this.editedIndex.id;
      this.closeDelete();
      db.collection("setup_data").doc(data_id).delete();
    },
    ShowItem(item) {
       console.log(item);
       this.center = [item.latitude, item.longitude]
    },
    editItem(item) {
       console.log(item);
       this.center = [item.latitude, item.longitude]
      // this.editedIndex = this.data.indexOf(item);
      // this.editedItem = Object.assign({}, item);
      
       this.dialogShow = true;


    },
  },
};
</script>

<style>
</style>