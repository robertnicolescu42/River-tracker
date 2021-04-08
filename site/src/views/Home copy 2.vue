<template>
  <div>
      <v-container>
          <div style="margin-bottom: 2em"> 
        <v-data-table
    :headers="arr"
    :items="test"
    :items-per-page="5"
    scrollable
    class="elevation-1"
  >
     <template v-slot:item="row">
          <tr>
            <td>{{row.item.date_time}}</td>
            <td>{{row.item.distance}}</td>
            <td>{{row.item.photo_path}}</td>
            <td>
            <!--Edit dialog --->
                <template>
                <v-row justify="center">
                    <v-dialog
                    :retain-focus="false"
                    v-model="dialog"
                    max-width="600px"
                    >
                    <template v-slot:activator="{ on, attrs }" >
                        <v-btn
                        fab
                        color="primary darken-2"
                        dark
                        v-bind="attrs"
                        v-on="on"
                        small
                        >
                        <v-icon>
                        mdi-circle-edit-outline
                        </v-icon>
                        </v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                        <span class="headline">Reading data</span>
                        </v-card-title>
                        <v-card-text>
                        <v-container>
                            <v-row>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                                <v-text-field 
                                v-model="newDistance"
                                :placeholder="row.item.distance"
                                label="Distance*"
                                hint="the distance read from the sensor: "
                                required
                                ></v-text-field>
                            </v-col>
                            </v-row>
                            <v-row>
                            <v-col
                                cols="12"
                                sm="6"
                            >
                            <v-container>
                                <v-date-picker
                                    v-model="newDateValue"
                                    year-icon="mdi-calendar-blank"
                                    prev-icon="mdi-skip-previous"
                                    next-icon="mdi-skip-next"
                                ></v-date-picker>
                            </v-container>
                            </v-col>
                            
                            <v-col>
                                <v-time-picker
                                v-model="newTimeValue"
                                format="24hr"
                                use-seconds
                                ></v-time-picker>
                            </v-col>
                            </v-row>
                        </v-container>
                        <small>*indicates required field</small>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn
                            color="red darken-1"
                            text
                            @click="deleteEntry(row.item.id)"
                        >
                            Delete
                        </v-btn>
                        <v-spacer></v-spacer>
                       
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="dialog = false"
                        >
                            Close
                        </v-btn>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="editEntryDistance(row.item.id, newDistance, newDateValue, newTimeValue)"
                        >
                            Save
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                    </v-dialog>
                </v-row>
                </template>
            <!--Edit dialog --->
            </td>
          </tr>
      </template>
  </v-data-table>
    <!-- sparkline -->
    <v-card max-width="1200" style="margin:0 auto; margin-top:4em">
      <v-sheet color="rgba(0, 0, 0, .12)">
        <v-sparkline
          :labels="labels"
          label-size="2.5"
          :value="values"
          color="rgba(255, 255, 255, .7)"
          height="80"
          padding="12.5"
          stroke-linecap="lineCap"
          smooth
          type="trend"
          :line-width="2.5"
          auto-draw
          auto-draw-duration="1000"
        >
        </v-sparkline>
      </v-sheet>
    </v-card>
    <!-- sparkline -->
    </div>
    </v-container>


  </div>

</template>

<script>
import {db} from "../firebase/db.js";
export default {
    data: ()=>({
        test:[],
        search:"",
        dialog: false,
        value: [
        ],       
        time: null,
        menu2: false,
        modal2: false,
        valDistance: 0,
        arr:[{
                text:'Date',
                align: 'start',
                value: 'date_time',
            },
            { text: 'Distance', value: 'distance' },
            { text: 'Photo Path', value: 'photo_path', sortable: false,},
            { text: 'Actions', value: 'action', sortable: false, align: 'center'}
            ],
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

        async deleteEntry(id){
            // if(confirm("Are you sure you want to delete this entry ?"))
                db.collection("distances").doc(id).delete();
                this.dialog = false;
        },

        async editEntryDistance(id, newDistanceValue, newDate, newTime){
                let newDateTimeValue = newDate + ' ' + newTime
                db.collection("distances").doc(id).update({
                    distance: parseInt(newDistanceValue),
                    date_time: newDateTimeValue
                });
                this.dialog = false
        }
    }
}
</script>

<style>

</style>