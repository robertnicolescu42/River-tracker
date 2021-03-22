<template>
  <div>
      
      <v-container>
    <div class="panel-body">
        
        <v-simple-table >
        <thead>
            <tr>
            <th>Date</th>
            <th>Distance</th>
            <th>Photo path</th>
            <th>Edit</th>
            <th>Delete</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="x in test" :key="x.id">
            <td>{{x.date_time}}</td>
            <td>{{x.distance}} cm</td>
            <td>{{x.photo_path}}</td>
            <td>
                <v-btn
                    color="primary"
                    v-bind="attrs"
                    v-on="on"
                    >
                    Edit
                </v-btn>
                <!-- <v-card>
                    <v-card-title>
                        <span class="headline"></span>
                    </v-card-title>
                </v-card> -->
            </td>
            <td>
                <template>
                    <v-row justify="center">
                        <v-dialog
                        v-model="dialog"
                        persistent
                        max-width="290"
                        >
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                            color="red"
                            dark
                            v-bind="attrs"
                            v-on="on"
                            >
                            Delete
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-title class="headline">
                            Do you really want to delete this entry?
                            </v-card-title>
                            <v-card-text>By pressing "Yes", the reading done at {{x.date_time}} will be deleted.</v-card-text>
                            <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                color="green darken-1"
                                text
                                @click="dialog = false"
                            >
                                No
                            </v-btn>
                            <v-btn
                                color="red darken-1"
                                text
                                @click="dialog = false; deleteName(x.id)"
                            >
                                Yes
                            </v-btn>
                            </v-card-actions>
                        </v-card>
                        </v-dialog>
                    </v-row>
                </template>
            </td>
            </tr>
        </tbody>
        </v-simple-table>
    </div>     
    
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)">
        <v-sparkline
          :labels="labels"
          label-size="2.5"
          :value="values"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="15"
          stroke-linecap="lineCap"
          smooth
          :line-width="2.5"
        >
          <!-- <template v-slot:label="values">
            {{ values.value }}cm
          </template> -->
        </v-sparkline>
      </v-sheet>
    </v-card-text>
      <!-- <v-container fluid="true">
        <div v-for="x in test" :key="x.id">
            <h1>merge</h1>
            <h3>{{x.distance}}</h3>
            <h3>{{x.photo_path}}</h3>
            <h3>{{x.date_time}}</h3>
            <v-btn @click="deleteName(x.id)" >Delete</v-btn>
            
        </div>
 -->
        <!-- <v-text-field background-color="blue"
        v-model="search"
        v-on:keyup.enter="execute()"
        ></v-text-field> -->
        <!-- </v-container> -->
      </v-container>
    <template>
        <v-footer>
            <v-col
            class="text-center"
            cols="12"
            >
            {{ new Date().getFullYear() }} — <strong>Nicolescu Robert</strong>
            </v-col>
        </v-footer>
    </template>
  </div>

  
</template>

<script>
import {db} from "../firebase/db.js";


export default {
    data: ()=>({
        test:[],
        search:"",
        value: [
        ],

        return: {
            dialog: false
        },
    }),
    
    firestore: {
        test: db.collection("distances").orderBy("date_time"),
        // test: db.collection("distances"),
    },

    computed:{
        values(){
            return this.test.map(x => x.distance);
        },

        labels(){
           return this.test.map(x => x.distance + "cm @" + x.date_time.substr(11,18)); 
        }
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
            // if(confirm("Are you sure you want to delete this entry ?"))
                db.collection("distances").doc(id).delete();
        }
    }
}
</script>

<style>

</style>