<template>
    <!-- message的z索引为2015 -->
    <el-menu style="position: fixed; width: 100%; height: 60px; top: 0; z-index: 2010;user-select: none;"
        mode="horizontal" :router="true" :default-active="menu_index">
        <el-menu-item index="/">
            <div class="logo" style="display: inline-flex;justify-content: center;align-items: center;">
                <el-image style="width: 52px; height: 52px;display: inline-flex;" :src="logo_1" :fit="'cover'" />
                <el-image style="width: 131px; height: 60px;display: inline-flex;" :src="logo_2" :fit="'cover'" />
            </div>
        </el-menu-item>
        <el-menu-item index="/ranking">
            <div class="header">{{ $t('menu.ranking') }}</div>
        </el-menu-item>
        <el-menu-item index="/video">
            <div class="header">{{ $t('menu.video') }}</div>
        </el-menu-item>
        <el-menu-item index="/world">
            <div class="header">{{ $t('menu.world') }}</div>
        </el-menu-item>
        <el-menu-item index="/guide">
            <div class="header">{{ $t('menu.guide') }}</div>
        </el-menu-item>
        <el-menu-item index="/score">
            <div class="header">{{ $t('menu.score') }}</div>
        </el-menu-item>
        <el-menu-item :index="player_url" :disabled="store.user.id == 0" @click="store.player = store.user;">
            <div class="header">{{ $t('menu.profile') }}</div>
        </el-menu-item>
        <LanguagePicker/>
        <div
            style="margin-left: auto;margin-right: 16px;display: inline-flex;justify-content: center;align-items: center;">
            <Menu @login="user_login" @logout="user_logout"></Menu>
        </div>
    </el-menu>


    <div class="common-layout">
        <el-container>
            <div class="header_all" style="padding-top: 0;overflow: hidden;">
                <div class="content" style="padding-top: 16px;">
                    <router-view />
                </div>
            </div>


            <el-footer style="margin: auto;">
                Copyright @ 2023　<a href="http://fff666.top">元扫雷网 fff666.top</a>　版权所有　<a
                    href="https://beian.miit.gov.cn/">苏ICP备2023056839号-1</a>
                <span style="width:12px; display:inline-block"></span>
                <a href="https://beian.mps.gov.cn/#/query/webSearch?code=32020602001691" rel="noreferrer"
                    target="_blank">苏公网安备32020602001691</a>
            </el-footer>
        </el-container>
    </div>

    <el-dialog draggable :lock-scroll="false" v-model="notice_visible" title="站长通知" width="30%"
        :before-close="handle_notice_close">
        <span>{{ notice }}</span>
        <template #footer>
            <span class="dialog-footer">
                <el-checkbox v-model="never_show_notice">不再显示此对话框</el-checkbox>
                <el-button type="primary" @click="handle_notice_close();">
                    确认
                </el-button>
            </span>
        </template>
    </el-dialog>
</template>

<script setup lang='ts'>
import { ref, reactive, onMounted, computed } from 'vue'
import Menu from "./components/Menu.vue";
import LanguagePicker from './components/LanguagePicker.vue';
// import { LoginStatus } from "@/utils/common/structInterface"
import useCurrentInstance from "@/utils/common/useCurrentInstance";
import { useUserStore } from './store'
const store = useUserStore()

import { useI18n } from 'vue-i18n';
const t = useI18n();

const { proxy } = useCurrentInstance();
const logo_1 = ref(require('@/assets/logo.png'))
const logo_2 = ref(require('@/assets/logo2.png'))

import { useRouter } from 'vue-router'
const router = useRouter()

// const player_visible = ref(false)
const notice_visible = ref(false)
const never_show_notice = ref(false)

// 主要是切换后的高亮
const menu_index = ref()

const notice = ref(`
1、即日起开始删档公测，公测与开发同步进行。公测结束后，在正式上线之前会删除所有数据。
2、相关意见、问题和建议请移步至此处[https://gitee.com/ee55/saolei_website/issues]发表。
`)


onMounted(() => {
    const notice_hash = localStorage.getItem("notice") as String;
    if (hash_code(notice.value) + "" != notice_hash) {
        notice_visible.value = true;
    }


    console.log(`
  元扫雷网(fff666.top)开发团队，期待您的加入: 2234208506@qq.com
  `);
    router.isReady().then(() => { menu_index.value = router.currentRoute.value.fullPath; })


})

const player_url = computed(() => {
    return '/player/' + store.user.id;
})

const user_login = () => {
    // player_visible.value = true;
    // tab_width.value = "14vw";
}

const user_logout = () => {
    // console.log(router.currentRoute.value.fullPath);
    // 如果切在我的地盘，就切到主页
    if (router.currentRoute.value.fullPath.slice(0, 7) == '/player') {
        menu_index.value = "/";
        proxy.$router.push("/");
    }
}

// const goback_home = () => {
//     router.push("/")
// }

// 站长通知关闭的回调
const handle_notice_close = () => {
    if (never_show_notice.value) {
        localStorage.setItem("notice", hash_code(notice.value) + "");
    }
    notice_visible.value = false;
}

const hash_code = function (t: string) {
    var hash = 0, i, chr;
    if (t.length === 0) return hash;
    for (i = 0; i < t.length; i++) {
        chr = t.charCodeAt(i);
        hash = ((hash << 5) - hash) + chr;
        hash |= 0; // 32bit integer
    }
    return hash;
};




</script>


<style lang='less'>
body {
    overflow-y: scroll;
    margin: 0;
}


.logo:hover {
    cursor: pointer;
}

.header {
    font-size: 18px;
}



/*设置点击前的样式 */
a {
    text-decoration: none;
    color: #000;
}

/*设置点击后的样式 */
.router-link-active {
    text-decoration: none;
    color: #000;
}

.header_all {
    margin: auto;
    width: 80vw;
}

.content {
    margin-top: 60px;
}

.clickable:hover {
    color: rgb(26, 127, 228);
    cursor: pointer;
}
</style>
