<template>
    <v-form class="text-center" style="width: 50%; margin-left: 25%;margin-top: 10%;">
        <v-container style="padding: 50px%;">
            <h3 class="text-indigo-600 font-mono text-center font-extrabold text-2xl"> Enterprise SignIn</h3>
        </v-container>
        <v-container style="padding: 50px">
            <v-text-field label="Email" variant="underlined" v-model="email" :rules="[rules.required]"></v-text-field>
            <v-text-field label="Password" variant="underlined" v-model="password" :rules="[rules.required,rules.password]"></v-text-field>
            <v-container style="width:50%;" class="text-center">
                <v-btn @click="signin()" class="text-white font-mono" color="indigo">SignIn</v-btn> 
            </v-container>
            <p class="font-mono text-xs text-center"> still haven't registered ?</p>
                <v-container style="width:50%;" class="py-2 px-4 rounded">
                    <NuxtLink to="/companyreg"><h3 class="text-rose-700 font-mono">SignUp</h3></NuxtLink>
                </v-container>
        </v-container>
    </v-form>
</template>

<script setup>
const password = ref("")
const email = ref("")
let rules = {
    required: (v) => !!v || "Required",
    password : (v) => (v.length >=8) || "Minimum 8 charactors required",
}
async function signin() { 
    console.log("signin",this.email, this.password)
}
</script>

<style lang="scss" scoped>

</style>