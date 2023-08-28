<template>
  <div class="rec">
    <Panel class="top-panel" :header="info.header">

      <table class="info">
        <tr>
          <td class="col1">Saving {{ group_data.save }}</td>
          <td class="col2">Tucking {{ group_data.tuck }}</td>
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

    <DataTable :value="fights" responsiveLayout="scroll" sortField="round" sort-order="1">
      <Column field="round" header="Rd" sortable></Column>
      <Column field="opponent" header="Opponent"></Column>
      <Column field="recommendation_hero" header="Hero" sortable sortField="rec.heroes_sort">
        <template #body="slotProps">
          <span v-if="slotProps.data.rec.heroes.length === 0 ">-</span>
          <span v-if="slotProps.data.rec.heroes.length !== 0">{{ slotProps.data.rec.heroes.join(',') }}</span>
        </template>
      </Column>
      <Column field="rec.flags" header="Flags" bodyStyle="text-align: left"></Column>
      <Column field="power_billions" header="Power" bodyStyle="text-align: left" sortable></Column>
      <Column field="members" header="Mem" bodyStyle="text-align: left"></Column>
    </DataTable>

  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component';
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
import {data} from "@/views/data";
import _ from "lodash";
import {Prop} from "vue-property-decorator";


@Options({
  components: {
    Button, Dialog, TabView, TabPanel, Card, Panel, Fieldset, DataTable, Column, TextArea, Toolbar,
    ConfirmDialog, InputText, Message, Accordion, AccordionTab
  },
})
export default class RecView extends Vue {
  @Prop({ default: 'rec_group_1' }) readonly group!: string
  info = data
  group_data = data['rec_group_1']
  fights = data['rec_group_1'].rounds;

  created() {
    this.group_data = data[this.group];
    this.fights = data[this.group].rounds;
  }

  summary() {
    const rounds = _
        .sortBy(this.fights, (fight: any) => {
          return fight.rec.heroes_sort;
        })
        .filter((fight: any) => {
          return (fight.rec.heroes.length > 0)
        })
        .map((fight: any) => {
          return fight.round;
        });

    let summ = `
      round_hero: ${this.roundHero()}
      <br><br>
      hero_round: ${this.heroRound()}
    `;

    if (this.info.additional_strategies) {
      summ += `
      <br><br>
      ${this.info.additional_strategies}
    `;
    }

    return summ;
  }

  roundHero() {
    const flags = _.map(this.info.flags_key, (desc, flag) => `${flag}_${desc}`).join('|')
    const info = `round_flag_hero (*=bottom hero and no flag) (${flags}):<br><br>`;
    const fights = _
        .sortBy(this.fights, (fight: any) => {
          return fight.round;
        })
        .map((fight: any) => {
          const heroes = fight.rec.heroes.join("&");
          if (fight.rec.heroes.length == 0) {
            return `${fight.round}_T`
          } else {
            return `${fight.round}_${heroes}`;
          }
        })
        .join('|');

    return fights;
  }

  heroRound() {
    const flags = _.map(this.info.flags_key, (desc, flag) => `${flag}_${desc}`).join('|')
    const info = `hero_flag_round (*=bottom hero and no flag) (${flags}):<br><br>`;

    const fights = _
        .sortBy(this.fights, (fight: any) => {
          return fight.rec.heroes_sort;
        })
        .map((fight: any) => {
          const heroes = fight.rec.heroes.join("&");
          if (fight.rec.heroes.length == 0) {
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
