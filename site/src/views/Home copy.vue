<template>
  <div>
      <v-container fluid="true">
        <div v-for="x in test" :key="x.id">
            <h1>merge</h1>
            <h1>{{x.distance}}</h1>
            <h1>{{x.photo_path}}</h1>
            <v-btn @click="deleteName(x.id)" >Delete</v-btn>
        </div>

        <v-text-field background-color="blue"
        v-model="search"
        v-on:keyup.enter="execute()"
        ></v-text-field>
        </v-container>
  </div>
  
</template>

<script>
import {db} from "../firebase/db.js";


export default {
    data: ()=>({
        test:[],
        search:""
    }),
    
    firestore: {
        test: db.collection("distances")
    },

    methods:{
        async execute(){
            if(this.search != ""){
                await db.collection("distances").add({
                    name: this.search,
                    location:""
                })
                this.search = ""
            }
        },

        async deleteName(id){
            db.collection("distances").doc(id).delete();
        }
    }
}
</script>

<style>

</style>