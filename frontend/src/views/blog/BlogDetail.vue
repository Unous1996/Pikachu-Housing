<template>
  <v-layout row wrap justify-space-between>
    <v-flex md8>
      <v-container>
        <v-flex>
          <v-breadcrumbs>
            <v-icon slot="divider">chevron_right</v-icon>

            <v-breadcrumbs-item
              v-for="crumb in crumbs"
              :disabled="crumb.disabled"
              :key="crumb.text"
              :to="crumb.to"
            >
              {{ crumb.text }}
            </v-breadcrumbs-item>
          </v-breadcrumbs>
        </v-flex>

        <v-layout>
          <v-flex row>
            <v-list-tile>
              <v-list-tile-avatar>
                <img :src="detail.avatar">
              </v-list-tile-avatar>
              <div>
                <div>
                  {{detail.username}}<br>
                  <span class="subtitle">{{detail.publishTime}}</span>
                </div>
              </div>
            </v-list-tile>
          </v-flex>
        </v-layout>

        <section class="content">
          <v-layout>
            <v-flex>
              <h1 class="detailTitle">{{detail.title}}</h1>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <v-flex class="mt-4">
            <div v-html="markdownContent(detail.content)" id="mdeditor"></div>
          </v-flex>
        </section>

        <section class="markdown-editor">
          <v-layout style="max-height: 500px;" column>
            <v-flex>
              <mavon-editor language="en"/>
            </v-flex>
            <v-flex md4>
              <v-list>
                 <v-btn class="primary align-right">Submit</v-btn>
                 <v-btn class="danger align-right">Reset</v-btn>
              </v-list>
            </v-flex>
            <v-divider></v-divider>
          </v-layout>
        </section>
      </v-container>
    </v-flex>

    <v-flex md3 v-if="$vuetify.breakpoint.mdAndUp" >
      <vmenu :content="this.tocObj"></vmenu>
    </v-flex>

  </v-layout>
</template>

<script>
import { marked } from '../../library/markedplus'
export default {
  name: 'BlogDetail',
  components: {
    'vmenu': () => import('./BlogMenu.vue'),
  },
  data () {
    return {
      crumbs: [
        {
          text: 'Home',
          disabled: false,
          to: '/'
        },
        {
          text: 'Blog list',
          disabled: false,
          to: '/blog/list'
        },
        {
          text: 'Link 2',
          disabled: true
        }
      ],
      detail: {
        avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
        username: 'LeBron James',
        publishTime: '1900/01/01',
        title: 'If you have a dream, do it right now.',
        content: '\n[TOC]\n' + '# Head1\n' +
        '\n' +
        '服了\n'  +
        '## Head2\n' +
        '\n' +
        '### Head3\n' +
        '\n' +
        '-----\n' +
        '\n' +
        '*斜体字*\n\n' +
        '### Head3\n' +
        '\n' +
        '**加粗字体**\n' +
        '\n' +
        '***加粗倾斜字体***\n' +
        '\n' +
        '~~ 删除线字体~~\n' +
        '\n' +
        '* 这个不知道什么文本形式*\\\n' +
        '\n' +
        '<small>这段是小字</small>\n' +
        '\n' +
        '传说中的单行长文字\n' +
        '\n' +
        '\n' +
        '> 引用文字\n' +
        '\n' +
        '\n' +
        '-----\n' +
        '\n' +
        '`高亮文字`\n' +
        '\n' +
        '***\n' +
        '\n' +
        '上面有条分割线\n' +
        '\n' +
        '\n' +
        '这段是脚注[^footer1]\n' +
        '\n' +
        '\n' +
        '\n' +
        '[链接文字例如百度](www.baidu.com)\n' +
        '\n' +
        '无序要点\n' +
        '\n' +
        '- 这是第一点\n' +
        '\n' +
        '- 这是第二点\n' +
        '\n' +
        '-  这是第三点\n' +
        '\n' +
        '\n' +
        '有序要点 \n' +
        '\n' +
        '1. 这是第一点\n' +
        '\n' +
        '2. 这是第二点\n' +
        '\n' +
        '3. 这是第三点\n'

      },
    }
  },
  methods: {
    markdownContent: (content) => {
      return marked(content, { sanitize: true })
    }
  }
}
</script>

<style scoped lang="less">
.subtitle {
  font-size: 10px;
  color: grey;
}
.content {
  padding: 16px;
  .detailTitle {
    font-size: 30px;
  }
}

.markdown-editor {
  padding: 16px;
}
</style>
