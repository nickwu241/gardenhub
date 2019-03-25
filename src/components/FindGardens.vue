<template>
  <section class="showcase">
    <div class="container-fluid p-0">
      <!-- <img
          class="img-fluid"
          src="https://www.c2dh.uni.lu/sites/default/files/styles/full_width/public/field/image/capture.png?itok=REb8jh_H"
      >-->
      <div class="col-12 showcase-text py-3">
        <div class="row mb-3">
          <div class="col-lg-3">
            <h2>Find a Garden</h2>
            <b-form class="mt-4 mb-5">
              <b-form-group id="pc-group" label="Near postal code" label-for="pc-input">
                <b-form-input
                  id="pc-input"
                  class="ml-2"
                  type="text"
                  v-model="form.postalcode"
                  required
                  placeholder="Enter Postal Code"
                />
              </b-form-group>
            </b-form>
            <p>
              I want to plant:
              <strong>{{ plantingFoods }}</strong>
            </p>
            <button
              :class="['btn', selectedFoodTypes.includes(foodType) ? 'btn-success' : 'btn-outline-success', 'ml-2', 'mb-2']"
              v-for="foodType in foodTypes"
              :key="foodType"
              @click="onFoodTypeClick(foodType)"
            >{{foodType}}</button>
          </div>

          <div class="col-lg-9">
            <div class="d-flex justify-content-center">
              <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d33041.70219608821!2d-123.08773063450637!3d49.26287174918186!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5486715b3a00673f%3A0xd6ad76f3bdd9853a!2sChina+Creek+North+Park!5e0!3m2!1sen!2sca!4v1553534406414"
                width="600"
                height="450"
                frameborder="0"
                style="border:0"
                allowfullscreen
              ></iframe>
            </div>
          </div>
        </div>

        <vue-good-table :columns="columns" :rows="rows" :line-numbers="true">
          <template slot="table-row" slot-scope="props">
            <span v-if="props.column.field == 'ACTIONS'">
              <button class="mr-2 btn btn-sm btn-info">View Details</button>
              <button
                class="btn btn-sm btn-primary"
                v-if="props.formattedRow['REGISTRATION_STATUS'].startsWith('Open')"
              >Join Garden</button>
              <button
                class="btn btn-sm btn-warning"
                v-if="props.formattedRow['REGISTRATION_STATUS'].startsWith('Waitlist')"
              >Join Waitlist</button>
            </span>
            <span v-else>{{props.formattedRow[props.column.field]}}</span>
          </template>
          <div slot="emptystate">There are no gardens matching the filters.</div>
        </vue-good-table>
      </div>
    </div>
  </section>
</template>

<script>
import rows from "../gardens.json";

const columns = [
  {
    label: "Type",
    field: "GARDEN_TYPE",
    width: "140px",
    filterOptions: {
      enabled: true,
      placeholder: "Any",
      filterValue: "",
      filterDropdownItems: ["Neighbourhood", "Youth"]
    }
  },
  // { label: "Id", field: "MAPID" },
  // { label: "Year", field: "YEAR_CREATED" },
  {
    label: "Name",
    field: "NAME",
    width: "200px",
    filterOptions: {
      enabled: true,
      placeholder: "Garden Name",
      filterValue: ""
    }
  },
  //   { label: "STREET_NUMBER", field: "STREET_NUMBER" },
  //   { label: "STREET_DIRECTION", field: "STREET_DIRECTION" },
  //   { label: "STREET_NAME", field: "STREET_NAME" },
  //   { label: "STREET_TYPE", field: "STREET_TYPE" },
  {
    label: "Addrress",
    field: "MERGED_ADDRESS",
    width: "200px",
    filterOptions: {
      enabled: true,
      placeholder: "Address",
      filterValue: ""
    }
  },
  // { label: "Lat", field: "LATITUDE" },
  // { label: "Lng", field: "LONGITUDE" },
  // { label: "# of plots", field: "NUMBER_OF_PLOTS" },
  // { label: "# of food trees", field: "NUMBER_OF_FOOD_TREES" },
  // { label: "Notes", field: "NOTES" },
  //   { label: "FOOD_TREE_VARIETIES", field: "FOOD_TREE_VARIETIES" },
  //   { label: "OTHER_FOOD_ASSETS", field: "OTHER_FOOD_ASSETS" },
  //   { label: "JURISDICTION", field: "JURISDICTION" },
  //   {
  //     label: "STEWARD_OR_MANAGING_ORGANIZATION",
  //     field: "STEWARD_OR_MANAGING_ORGANIZATION"
  //   },
  // { label: "Email", field: "PUBLIC_E_MAIL" },
  // { label: "Website", field: "WEBSITE" }
  {
    label: "Status",
    field: "REGISTRATION_STATUS",
    width: "80px",
    filterOptions: {
      enabled: true,
      placeholder: "Any",
      filterValue: "Open", // initial populated value for this filter
      filterDropdownItems: ["Waitlist", "Open"]
    }
  },
  { label: "Actions", field: "ACTIONS", width: "140px" }
];

export default {
  data() {
    return {
      columns,
      rows,
      foodTypes: [
        "Beets",
        "Carrots",
        "Cauliflower",
        "Peppers",
        "Potatoes",
        "Pumpkins",
        "Strawberries",
        "Tomatoes"
      ],
      selectedFoodTypes: ["Beets"],
      form: {
        postalcode: "V6H 1G5"
      }
    };
  },
  computed: {
    plantingFoods: function() {
      if (this.selectedFoodTypes.length == 0) {
        return "anything";
      }

      return this.selectedFoodTypes.join(", ");
    }
  },
  methods: {
    onFoodTypeClick: function(foodType) {
      if (this.selectedFoodTypes.includes(foodType)) {
        this.selectedFoodTypes.splice(
          this.selectedFoodTypes.indexOf(foodType),
          1
        );
      } else {
        this.selectedFoodTypes.push(foodType);
        this.selectedFoodTypes.sort();
      }
    }
  }
};
</script>

<style scoped>
</style>