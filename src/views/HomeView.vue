<template>
  <div class="home">
    <Panel class="top-panel" :header="info.header" :toggleable="true">
      <table class="info">
        <tr>
          <td class="col1">Num Top Heroes Save</td>
          <td class="col2">{{ info.num_heroes_to_save }}</td>
        </tr>
        <tr>
          <td class="col1">Num Tucking Rounds</td>
          <td class="col2">{{ info.num_rounds_tucking }}</td>
        </tr>
        <tr>
          <td class="col1">Num Exception Rounds</td>
          <td class="col2">{{ info.num_exception_rounds }}</td>
        </tr>
        <tr v-for="(value, name) in info.flags_key" v-bind:key="name">
          <td class="col1">Flag <span class="text-primary">{{ name }}</span></td>
          <td class="col2">{{ value }}</td>
        </tr>
      </table>
    </Panel>

    <Panel header="For alliance chat/board" class="p">
      <div class="break-word" v-html="summary()"></div>
    </Panel>

    <Panel header="Click on Rd and Hero columns to sort" class="p">
    </Panel>

    <DataTable :value="fights" responsiveLayout="scroll" sortField="recommendation_heroes_sort" sort-order="1">
      <Column field="round" header="Rd" sortable></Column>
      <Column field="opponent" header="Opponent"></Column>
      <Column field="recommendation_hero" header="Hero" sortable sortField="recommendation_heroes_sort">
        <template #body="slotProps">
          <span v-if="slotProps.data.recommendation_heroes.length === 0 ">-</span>
          <span v-if="slotProps.data.recommendation_heroes.length !== 0">{{ slotProps.data.recommendation_heroes.join(',') }}</span>
        </template>
      </Column>
      <Column field="recommendation_flags" header="Flags" bodyStyle="text-align: left"></Column>
      <Column field="power_billions" header="Power" bodyStyle="text-align: left"></Column>
      <Column field="members" header="Mem" bodyStyle="text-align: left"></Column>
<!--      <Column field="server" header="Server" bodyStyle="text-align: left"></Column>-->
<!--      <Column field="comment" header="Comm" bodyStyle="text-align: left"></Column>-->
    </DataTable>

<!--    <Panel header="Round_Hero">-->
<!--      <div class="break-word" v-html="roundHero()"></div>-->
<!--    </Panel>-->
<!--    <Panel header="Hero_Round">-->
<!--      <div class="break-word" v-html="heroRound()"></div>-->
<!--    </Panel>-->

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

  summary() {
    const rounds = _
        .sortBy(this.fights, (fight: any) => {
          return fight.recommendation_heroes_sort;
        })
        .filter((fight: any) => {
          return (fight.recommendation_heroes.length > 0)
        })
        .map((fight: any) => {
          return fight.round;
        });

    const summ = `
      |round_hero| -> ${this.roundHero()}
      <br><br>
      |hero_round| -> ${this.heroRound()}
      <br><br>
      ${this.info.additional_strategies}
      <br><br>
      https://kt402.github.io for more details.
    `;
/*
<td class="col2">{{ info.num_heroes_to_save }}</td>
        </tr>
        <tr>
          <td class="col1">Tucking</td>
          <td class="col2">{{ info.num_rounds_tucking }}</td>
 */
    return summ;
  }

  roundHero() {
    const flags = _.map(this.info.flags_key, (desc, flag) => `${flag}_${desc}`).join('|')
    const info = `round_flag_hero (*=bottom hero and no flag) (${flags}):<br><br>`;
    const fights = _
        .map(this.fights,
            (fight: any) => {
              const heroes = fight.recommendation_heroes.join("&");
              if (fight.recommendation_heroes.length == 0) {
                return `${fight.round}_T`
              } else {
                return `${fight.round}_${heroes}`;
              }
            }
        )
        .join('|');

    return fights;
  }

  heroRound() {
    const flags = _.map(this.info.flags_key, (desc, flag) => `${flag}_${desc}`).join('|')
    const info = `hero_flag_round (*=bottom hero and no flag) (${flags}):<br><br>`;

    const fights = _
        .sortBy(this.fights, (fight: any) => {
          return fight.recommendation_heroes_sort;
        })
        .map((fight: any) => {
          const heroes = fight.recommendation_heroes.join("&");
          if (fight.recommendation_heroes.length == 0) {
            return `T_${fight.round}`
          } else {
            return `${heroes}_${fight.round}`;
          }
        })
        .join('|');

    return fights;
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

//.top-panel .p-panel-content {
.p-panel-content {
  padding: .5rem .5rem !important;
}

//.top-panel .p-panel-header {
.p-panel-header {
  padding: .5rem .5rem !important;
}

.p-panel {
  font-size: .8rem !important;
}



.p-datatable .p-sortable-column .p-sortable-column-icon {
  font-size: .65rem !important;
  margin-left: 0 !important;
}

</style>
