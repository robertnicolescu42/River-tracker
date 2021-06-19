<template>
  <div>
    <!-- sparkline -->
    <v-card style="margin: 0 auto; margin-top: 0.2em; margin-bottom: 0.5em">
      <v-sheet color="rgba(0, 0, 0, .12)">
        <v-sparkline
          :labels="labels.reverse()"
          label-size="2.5"
          :value="values.reverse()"
          color="rgba(255, 255, 255, .7)"
          height="60"
          padding="19.5"
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

    <v-data-table
      :headers="headers"
      :items="data"
      update:sort-desc
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title
            >Recent readings show that {{ recentAverage() }}</v-toolbar-title
          >
          <!-- <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider> -->
          <v-spacer></v-spacer>
          <!-- edit/delete dialogue -->
          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.distance"
                        label="Distance"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">
                  Cancel
                </v-btn>
                <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-dialog v-model="dialogShow" max-width="800px">
            <v-card>
              <v-card-title>
                <span class="headline">Photo</span>
              </v-card-title>

              <v-card-text>
                <v-container style="display: flex; justify-content: center">
                  <img
                    :src="`data:image/png;base64,${editedItem.photo_path}`"
                    width="500"
                    height="500"
                  /><!-- image decoding -->
                </v-container>
              </v-card-text>

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
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <!-- edit/delete dialogue -->
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="ShowItem(item)"> mdi-eye </v-icon>
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
    </v-data-table>

    <!-- <pre
      {{data}}
  </pre> -->
  </div>
</template>

<script>
import { db } from "../firebase/db.js";
//TIME FUNCTIONS
function last3MonthsDate() {
  var today = new Date();
  var lastWeek = new Date(
    today.getFullYear(),
    today.getMonth() - 3,
    today.getDate()
  );
  var lastWeekMonth = lastWeek.getMonth() + 1;
  var lastWeekDay = lastWeek.getDate();
  var lastWeekYear = lastWeek.getFullYear();

  var last3MonthsDisplayPadded =
    ("0000" + lastWeekYear.toString()).slice(-4) +
    "-" +
    ("00" + lastWeekMonth.toString()).slice(-2) +
    "-" +
    ("00" + lastWeekDay.toString()).slice(-2);
  return last3MonthsDisplayPadded;
}

export default {
  components: {},
  data: () => ({
    dialogShow: false,
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: "Date", value: "date_time" },
      { text: "Distance (cm)", value: "distance" },
      // { text: 'Photo Path', value: 'photo_path',sortable: false },
      { text: "Actions", value: "actions", sortable: false },
    ],
    data: [],
    data1: [],
    riverData: [],
    editedIndex: -1,
    editedItem: {},
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },

    values() {
      return this.data.slice(-8).map((x) => x.distance);
      // return this.data.map(x => x.distance);
    },

    labels() {
      return this.data.map(
        (x) => x.distance + "cm @" + x.date_time.substr(11, 18)
      );
      //  return this.data.map(x => x.distance + "cm @" + x.date_time.substr(0,10));
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  methods: {
    editItem(item) {
      console.log(item);
      this.editedIndex = this.data.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    ShowItem(item) {
      console.log(item);
      this.editedIndex = this.data.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogShow = true;
    },

    deleteItem(item) {
      console.log(item);
      this.editedIndex = item;
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      let data_id = this.editedIndex.id;
      this.closeDelete();
      db.collection("distances").doc(data_id).delete();
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

    save() {
      if (this.editedIndex > -1) {
        // Object.assign(this.data[this.editedIndex], this.editedItem);
        let data_id = this.data[this.editedIndex].id;
        let newDistanceValue = this.editedItem.distance;
        db.collection("distances")
          .doc(data_id)
          .update({
            distance: parseFloat(newDistanceValue),
            date_time: this.data[this.editedIndex].date_time,
            photo_path: this.data[this.editedIndex].photo_path,
          });
      } else {
        this.data.push(this.editedItem);
      }
      this.close();
    },

    todayDateFormatted() {
      var today = new Date();
      var lastWeek = new Date(
        today.getFullYear(),
        today.getMonth(),
        today.getDate()
      );
      var lastWeekMonth = lastWeek.getMonth() + 1;
      var lastWeekDay = lastWeek.getDate();
      var lastWeekYear = lastWeek.getFullYear();

      var lastDayDisplayPadded =
        ("0000" + lastWeekYear.toString()).slice(-4) +
        "-" +
        ("00" + lastWeekMonth.toString()).slice(-2) +
        "-" +
        ("00" + lastWeekDay.toString()).slice(-2);
      return lastDayDisplayPadded;
    },
    recentAverage() {
      // lastDayDate()
      var sum = 0;
      var array = this.data.slice(-10);
      for (var i = 0; i < 10; i++) {
        sum += parseInt(array[i].distance, 10);
      }
      // console.log(array);

      var avg = sum / 10;
      let low_bound = this.riverData[0].low_bound;
      let high_bound = this.riverData[0].high_bound;
      if (low_bound <= avg && avg <= high_bound)
        return (
          "the river is in normal conditions: " +
          avg.toString() +
          "cm height, between " +
          low_bound.toString() +
          "cm and " +
          high_bound.toString() +
          "cm."
        );
      return (
        "the river is in abnormal conditions: " +
        avg.toString() +
        "cm height, not between " +
        low_bound.toString() +
        "cm and " +
        high_bound.toString() +
        "cm."
      );
    },
  },
  firestore: {
    // data: db.collection("distances").orderBy("date_time", "desc"),
    data: db
      .collection("distances")
      .where("date_time".substr(0, 10), ">=", last3MonthsDate())
      .orderBy("date_time", "desc"), //dataset for last month
    // test: db.collection("distances"),

    riverData: db.collection("setup_data").where("device_id", "==", 1),
  },
};
</script>

<style>
</style>