<template>
<v-container>
    

     <v-card>
    <v-tabs
      v-model="tab"
      background-color="transparent"
      color="basil"
      grow
    >
      <v-tab>Last Day</v-tab>
      <v-tab>Last Week</v-tab>
      <v-tab>Last Month</v-tab>
      <v-tab>Last 3 Months</v-tab>
      <!-- last day -->
      <v-tab-item> 
        <v-container fluid>
              <lastDay></lastDay>
        </v-container>
      </v-tab-item>
      <!-- last day -->

      <!-- last week -->
      <v-tab-item> 
        <v-container fluid>
              <lastWeek></lastWeek>
        </v-container>
      </v-tab-item>
      <!-- last week -->

      <!-- last month -->
      <v-tab-item> 
        <v-container fluid>
              <lastMonth></lastMonth>
        </v-container>
      </v-tab-item>
      <!-- last month -->

      <!-- last 3 months -->
      <v-tab-item> 
        <v-container fluid>
              <last3Months></last3Months>
        </v-container>
      </v-tab-item>
      <!-- last 3months -->
    </v-tabs>
  </v-card>






</v-container>
</template>
<script>
export default {
  components: {},
  data() {
    return {};
  },
};
</script>