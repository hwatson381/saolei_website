import type { VueMessageType } from 'vue-i18n'
import { LocaleMessage } from '@intlify/core-base'

/**
 * 配置语法：https://vue-i18n.intlify.dev/guide/essentials/syntax.html
 */
export type LocaleConfig = LocaleMessage<VueMessageType> & {
    // 当前语言唯一标识
    local: string,
    // 嵌套配置示例 TODO 删除嵌套配置示例
    name: string,
    common: {
        level: {
            b: string,
            i: string,
            e: string,
        },
        mode: {
            standard: string,
            noFlag: string,
            noGuess: string,
            recursive: string
        }
        prop: {
            action: string,
            designator: string,
            fileName: string,
            level: string,
            status: string,
            time: string,
        }
    },
    forgetPassword: {
        title: string,
        email: string,
        captcha: string,
        getEmailCode: string,
        emailCode: string,
        password: string,
        confirmPassword: string,
        confirm: string
    },
    login: {
        title: string,
        username: string,
        password: string,
        captcha: string,
        forgetPassword: string,
        keepMeLoggedIn: string,
        confirm: string
    },
    menu: {
        ranking: string,
        video: string,
        world: string,
        guide: string,
        score: string,
        profile: string,
        welcome: string,
        login: string,
        logout: string,
        register: string,
        downloads: string,
        links: string,
        team: string
    },
    profile: {
        changeAvatar: string,
        realname: string,
        realnameInput: string,
        signature: string,
        signatureInput: string,
        change: string,
        confirmChange: string,
        cancelChange: string,
        designator: string,
        records: {
            title: string,
            modeRecord: string
        }
        videos: string,
        upload: {
            title: string,
            dragOrClick: string,
            uploadAll: string,
            cancelAll: string,
            constraintNote: string,
            error: {
                collision: string,
                custom: string,
                designator: string,
                fail: string,
                fileext: string,
                filename: string,
                filesize: string,
                pass: string,
                process: string,
                upload: string,
            }
        }
    },
    register: {
        title: string,
        username: string,
        email: string,
        captcha: string,
        getEmailCode: string,
        emailCode: string,
        password: string,
        confirmPassword: string,
        agreeTo: string,
        termsAndConditions: string,
        confirm: string
    },
}
