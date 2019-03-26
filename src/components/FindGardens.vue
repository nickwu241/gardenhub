<template>
  <div>
    <!-- Navigation -->
    <nav class="navbar navbar-dark bg-success">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Garden Hub</a>
        <form class="form-inline">
          <ul class="navbar-nav mr-4">
            <li class="navbar-item active">
              <a href="#" class="nav-link">Manage Crops</a>
            </li>
          </ul>
          <button
            class="btn btn-primary my-2 my-sm-0"
            type="button"
            @click="() => this.$router.push('/')"
          >Logout</button>
        </form>
      </div>
    </nav>

    <!-- Find Gardens Section-->
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
                    type="text"
                    v-model="form.postalcode"
                    required
                    placeholder="Enter Postal Code"
                    :state="postalcodeValidation"
                  />
                  <b-form-invalid-feedback :state="postalcodeValidation">
                    Must be exactly 6 characters.
                    <br>For example: V5T1E5
                  </b-form-invalid-feedback>
                  <b-form-valid-feedback :state="postalcodeValidation">Postal code looks good.</b-form-valid-feedback>
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
                  :src="imgsrc"
                  width="800"
                  height="600"
                  frameborder="0"
                  style="border:0"
                  allowfullscreen
                ></iframe>
              </div>
            </div>
          </div>

          <vue-good-table
            :columns="columns"
            :rows="rows"
            :line-numbers="true"
            @on-row-click="onRowClick"
          >
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
  </div>
</template>

<script>
import rows from "../gardens.json";
import rows_v5t1e5 from "../gardens-v5t1e5.json";

const kChinaCreekNorthParkMapId = "FA031";
const imgsrc = {
  default:
    "https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d47172.652263796466!2d-123.12587775189185!3d49.25812170877924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1svancouver+Community+gardens!5e0!3m2!1sen!2sca!4v1553597006222",
  v5t1e5:
    "https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d12791.955974750907!2d-123.0903669815998!3d49.26469957071422!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1svancouver+community+gardens!5e0!3m2!1sen!2sca!4v1553597450136",
  chinaCreekNorthPark:
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d9590.984649020796!2d-123.09051619442711!3d49.26424495982161!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5486715b3a00673f%3A0xd6ad76f3bdd9853a!2sChina+Creek+North+Park!5e0!3m2!1sen!2sca!4v1553598768980"
};

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
      filterValue: "",
      filterDropdownItems: ["Waitlist", "Open"]
    }
  },
  { label: "Actions", field: "ACTIONS", width: "140px" }
];

export default {
  data() {
    return {
      columns,
      imgsrcUrl: null,
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
      selectedFoodTypes: [],
      form: {
        postalcode: ""
      }
    };
  },
  computed: {
    plantingFoods: function() {
      if (this.selectedFoodTypes.length == 0) {
        return "Anything";
      }

      return this.selectedFoodTypes.join(", ");
    },
    postalcodeValidation: function() {
      if (this.form.postalcode.length == 0) {
        return null;
      }
      return this.form.postalcode.length == 6;
    },
    imgsrc: function() {
      if (this.imgsrcUrl != null) {
        return this.imgsrcUrl;
      }
      if (this.form.postalcode === "V5T1E5") {
        return imgsrc["v5t1e5"];
      }
      return imgsrc["default"];
    },
    rows: function() {
      if (this.form.postalcode === "V5T1E5") {
        return rows_v5t1e5;
      }
      return rows;
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
    },
    onRowClick(params) {
      if (params.row && params.row["MAPID"] === kChinaCreekNorthParkMapId) {
        this.imgsrcUrl = imgsrc["chinaCreekNorthPark"];
      } else {
        this.imgsrcUrl = null;
      }
    }
  }
};
</script>

<style scoped>
</style>