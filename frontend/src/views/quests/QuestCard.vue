<template>
    <v-card class="elevation-8">
        <v-img :src="quest.preview" :aspect-ratio="16/9">
        </v-img>
                    <v-card-title v-text="quest.title"/>

        <v-card-text>
            <v-list>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-map</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ quest.place }}</v-list-item-title>
                        <v-list-item-subtitle>Место проведения</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-map-marker-multiple</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ quest.count_of_cp }}</v-list-item-title>
                        <v-list-item-subtitle>Количество КП</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-calendar</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ dateStart }}</v-list-item-title>
                        <v-list-item-subtitle>Дата проведения</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-timelapse</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ duration }}</v-list-item-title>
                        <v-list-item-subtitle>Продолжительность</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card-text>
        <v-divider/>
        <v-card-actions md-alignment="space-between">
            <v-btn color="primary" @click="navigateToStatistic(quest.id)">Статистика</v-btn>
            <v-spacer/>
            <v-btn color="accent" @click="edit(quest.id)">Редактировать</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: 'QuestCard',
        props: ['quest'],
        methods: {
            edit(id) {
                this.$router.push({name: 'editQuest', params: {id: id}})
            },
            navigateToStatistic(id) {
                this.$router.push({name: 'statistic', params: {id: id}})
            }
        },
        computed: {
            dateStart: function () {
                console.log(`start time ${this.quest.start_time}`);
                const start_time = new Date(this.quest.start_time).toISOString();
                return start_time.substr(0, 10) + ", " + start_time.substr(11, 5)
            },
            duration: function () {
                return new Date('1970-01-01T' + this.quest.duration + 'Z').toISOString().substr(11, 5)
            }
        }
    }
</script>
