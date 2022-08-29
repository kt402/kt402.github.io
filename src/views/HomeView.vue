<template>
  <div class="home">
    <Message severity="info">Saving 4 heroes for playoffs, so top hero used is #5.</Message>
    <Message severity="info">
      Recommended Flags
      <ul>
        <li>SC - Strategy or Courage</li>
        <li>BSC - Brutality, Strategy, or Courage</li>
        <li>* - Any</li>
        <li>x - None</li>
      </ul>
    </Message>
    <Message severity="info">
      <div class="mb-2">Round-Hero; -> {{ roundHero() }}</div>
      <div class="mb-2">Hero-Round; -> {{ heroRound() }}</div>
      <div>Recommending strategy/courage for more top heroes, and anything (if you want to save strategy/courage) for bottom. And specifically for round 7 could also use brutality.</div>
    </Message>
    <DataTable :value="fights" responsiveLayout="scroll">
      <Column field="round" header="Round" bodyStyle="text-align: center"></Column>
      <Column field="opponent" header="Opp"></Column>
      <Column field="recommendation_hero" header="Hero#" bodyStyle="text-align: center">
        <template #body="slotProps">
          <span v-if="slotProps.data.recommendation_hero === -1">TUCK</span>
          <span v-if="slotProps.data.recommendation_hero !== -1">{{ slotProps.data.recommendation_hero}}</span>
        </template>
      </Column>
<!--      <Column field="brand" header="Brand">-->
<!--        <template #body="slotProps">-->
<!--          <img :src="'demo/images/car/' + slotProps.data.brand + '.png'" :alt="slotProps.data.brand"  width="48px"/>-->
<!--        </template>-->
<!--      </Column>-->
      <Column field="recommendation_flags" header="Flags" bodyStyle="text-align: center"></Column>
      <Column field="server" header="Server" bodyStyle="text-align: center"></Column>
      <Column field="power_billions" header="Power(B)" bodyStyle="text-align: center"></Column>
      <Column field="members" header="Members" bodyStyle="text-align: center"></Column>
    </DataTable>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component';
import store from "@/store";
import Dialog from "primevue/dialog";
import Button from "primevue/button";
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";
import Card from "primevue/card";
import Panel from "primevue/panel";
import Fieldset from "primevue/fieldset";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import TextArea from "primevue/textarea";
import Toolbar from "primevue/toolbar";
import InputText from "primevue/inputtext";
import ConfirmDialog from "primevue/confirmdialog";
import Message from "primevue/message";
// import firebase from "@/firebaseInit";
import { doc, setDoc } from "firebase/firestore";
import { getAuth, onAuthStateChanged, signInWithEmailAndPassword, User, AuthCredential, UserCredential, signOut } from "firebase/auth";
// import {db} from "@/store/db";
import {data} from "@/views/data";
import _ from "lodash";


@Options({
  components: {
    Button, Dialog, TabView, TabPanel, Card, Panel, Fieldset, DataTable, Column, TextArea, Toolbar,
    ConfirmDialog, InputText, Message,
  },
})
export default class HomeView extends Vue {
  fights = data

  // login() {
  //   const auth = getAuth(firebase);
  //   signInWithEmailAndPassword(auth, "", "").then((userCredential: UserCredential) => {
  //     console.log(userCredential.user);
  //   }).catch((error) => {
  //     console.error(error);
  //   });
  // }
  //
  // logout() {
  //   const auth = getAuth(firebase);
  //   signOut(auth);
  // }
  //
  // testData() {
  //   const cityRef = doc(db, 'cities', 'BJ');
  //   setDoc(cityRef, { capital: true }, { merge: true });
  // }

  roundHero() {
    return _
        .map(this.fights, (fight: any) => `${fight.round}-${(fight.recommendation_hero == -1) ? 'TUCK' : fight.recommendation_hero}`)
        .join(';');
  }

  heroRound() {
    return _
        .sortBy(this.fights, (fight: any) => fight.recommendation_hero)
        .map((fight: any) => `${(fight.recommendation_hero == -1) ? 'TUCK' : fight.recommendation_hero}-${fight.round}`)
        .join(';');
  }
}

</script>

<style>
.p-datatable-tbody, .p-datatable-thead {
  font-size: .8rem;
}

.p-datatable .p-datatable-tbody > tr > td {
  padding: .5rem .3rem !important;
}
</style>
