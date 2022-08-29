<template>
  <div class="home">
    <Panel class="top-panel" header="AC_Dec.12.2022" :toggleable="true">
      <table class="info">
        <tr>
          <td class="col1">Saving</td>
          <td class="col2">{{ info.num_heroes_to_save }}</td>
        </tr>
        <tr>
          <td class="col1">Tucking</td>
          <td class="col2">{{ info.num_rounds_tucking }}</td>
        </tr>
        <tr>
          <td class="col1">Flags</td>
          <td class="col2">strat/courage (brut if weak)</td>
        </tr>
      </table>
    </Panel>

    <DataTable :value="fights" responsiveLayout="scroll">
      <Column field="round" header="Round"></Column>
      <Column field="opponent" header="Opp"></Column>
      <Column field="recommendation_hero" header="Hero">
        <template #body="slotProps">
          <span v-if="slotProps.data.recommendation_hero === 0">-</span>
          <span v-if="slotProps.data.recommendation_hero !== 0">{{ slotProps.data.recommendation_hero}}</span>
        </template>
      </Column>
      <Column field="recommendation_flags" header="Flags" bodyStyle="text-align: left"></Column>
      <Column field="server" header="Server" bodyStyle="text-align: left"></Column>
      <Column field="power_billions" header="Power" bodyStyle="text-align: left"></Column>
    </DataTable>

    <Panel header="Round_Hero">
      <div class="break-word">Round_Hero(*=tuck): {{ roundHero() }}</div>
    </Panel>
    <Panel header="Hero_Round">
      <div class="break-word">Hero_Round(*=tuck): {{ heroRound() }}</div>
    </Panel>

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
import Accordion from "primevue/accordion";
import AccordionTab from "primevue/accordiontab";
// import firebase from "@/firebaseInit";
import { doc, setDoc } from "firebase/firestore";
import { getAuth, onAuthStateChanged, signInWithEmailAndPassword, User, AuthCredential, UserCredential, signOut } from "firebase/auth";
// import {db} from "@/store/db";
import {data} from "@/views/data";
import _ from "lodash";


@Options({
  components: {
    Button, Dialog, TabView, TabPanel, Card, Panel, Fieldset, DataTable, Column, TextArea, Toolbar,
    ConfirmDialog, InputText, Message, Accordion, AccordionTab
  },
})
export default class HomeView extends Vue {
  info = data
  fights = data.rounds

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
        .map(this.fights,
            (fight: any) => {
              return `${fight.round}_${(fight.recommendation_hero == 0) ? '*' : fight.recommendation_hero}`;
            }
        )
        .join('|');
  }

  heroRound() {
    return _
        .sortBy(this.fights, (fight: any) => {
          return (fight.recommendation_hero == 0) ? 99 : fight.recommendation_hero;
        })
        .map((fight: any) => {
          return `${(fight.recommendation_hero == 0) ? '*' : fight.recommendation_hero}_${fight.round}`;
        })
        .join('|');
  }
}

</script>

<style lang="scss">
.p-datatable-tbody, .p-datatable-thead {
  font-size: .8rem;
}

.p-datatable .p-datatable-tbody > tr > td {
  padding: .5rem .3rem !important;
}

.p-datatable .p-datatable-thead > tr > th {
  padding: .5rem .3rem !important;
}

.p-card-body {
  padding: 1rem 1rem 0.1rem 1rem !important;
}

.p-card-content {
  padding: 0 !important;
}

.break-word {
  overflow-wrap: anywhere;
  word-break: break-all;
}

.info {
  width: 100%;
}

.info {
  tr:nth-child(odd) {
    background-color: var(--gray-800);
  }
  td:nth-child(1) {
    overflow: hidden;
    white-space: nowrap;
    width: 5rem;
  }
}

.top-panel .p-panel-content {
  padding: 0 .5rem !important;
}

.top-panel .p-panel-header {
  padding: 0 .5rem !important;
}

.p-panel {
  font-size: .8rem !important;
}

</style>
