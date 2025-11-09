<template>
  <div class="flex h-screen bg-gradient-to-br from-gray-50 to-gray-100">
    <!-- Sidebar -->
    <aside
      :class="[
        sidebarOpen ? 'w-64' : 'w-20',
        'bg-white shadow-2xl transition-all duration-300 ease-in-out flex flex-col relative'
      ]"
    >
      <!-- Logo / Brand -->
      <div
        class="h-16 flex items-center justify-between px-4 border-b border-gray-200 bg-gradient-to-r from-blue-600 to-purple-600"
      >
        <span v-if="sidebarOpen" class="text-xl font-bold text-white tracking-wide">
          Skill Passport
        </span>
        <button
          @click="sidebarOpen = !sidebarOpen"
          class="p-2 rounded-lg hover:bg-white/20 transition-colors"
        >
          <component
            :is="sidebarOpen ? 'XIcon' : 'MenuIcon'"
            class="w-5 h-5 text-white"
          />
        </button>
      </div>

      <!-- Navigation -->
      <nav class="flex-1 p-3 space-y-2 overflow-y-auto">
        <button
          v-for="item in navItems"
          :key="item.id"
          @click="activeTab = item.id"
          :class="[
            'w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 group',
            activeTab === item.id
              ? `bg-gradient-to-r ${item.color} text-white shadow-lg transform scale-105`
              : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
          ]"
        >
          <component :is="item.icon" class="w-5 h-5" />
          <span v-if="sidebarOpen" class="font-medium">{{ item.label }}</span>
        </button>
      </nav>

      <!-- User Profile -->
      <div
        v-if="sidebarOpen"
        class="p-4 border-t border-gray-200 bg-gradient-to-r from-gray-50 to-gray-100"
      >
        <div
          class="flex items-center gap-3 p-3 rounded-xl bg-white shadow-md hover:shadow-lg transition-shadow"
        >
          <img
            src="https://i.pravatar.cc/40"
            alt="Profile"
            class="w-10 h-10 rounded-full ring-2 ring-blue-500"
          />
          <div class="flex-1">
            <p class="text-sm font-semibold text-gray-800">Adarsh</p>
            <p class="text-xs text-gray-500">Premium User</p>
          </div>
        </div>
      </div>
    </aside>

    <!-- Main content area -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <!-- Navbar -->
      <header class="h-16 bg-white shadow-lg flex items-center justify-between px-6 z-10">
        <div class="flex items-center gap-4 flex-1">
          <h1
            class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent"
          >
            {{ currentTab.label }}
          </h1>
          <div
            class="hidden md:flex items-center gap-2 bg-gray-100 rounded-full px-4 py-2 flex-1 max-w-md"
          >
            <SearchIcon class="w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Search anything..."
              class="bg-transparent border-none outline-none text-sm flex-1"
            />
          </div>
        </div>

        <div class="flex items-center gap-4">
          <button class="p-2 rounded-full hover:bg-gray-100 transition-colors relative">
            <BellIcon class="w-5 h-5 text-gray-600" />
            <span class="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
          </button>

          <div
            class="flex items-center gap-3 px-3 py-2 rounded-full hover:bg-gray-100 transition-colors cursor-pointer"
          >
            <img
              src="https://i.pravatar.cc/40"
              alt="User Avatar"
              class="w-9 h-9 rounded-full ring-2 ring-blue-500"
            />
            <span class="font-medium text-gray-700">Adarsh</span>
            <ChevronDownIcon class="w-4 h-4 text-gray-500" />
          </div>
        </div>
      </header>

      <!-- Dynamic Content -->
      <main class="flex-1 p-6 overflow-y-auto">
        <div v-if="activeTab === 'dashboard'" class="space-y-6 animate-fadeIn">
          <!-- Stats Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div
              v-for="(stat, i) in stats"
              :key="i"
              :class="`${stat.color} rounded-2xl p-6 text-white shadow-xl transform hover:scale-105 transition-all duration-300 hover:shadow-2xl`"
            >
              <p class="text-sm font-medium opacity-90">{{ stat.label }}</p>
              <p class="text-4xl font-bold mt-2">{{ stat.value }}</p>
              <p class="text-xs mt-3 opacity-80">{{ stat.change }}</p>
            </div>
          </div>

          <!-- Recent Activity -->
          <div class="bg-white rounded-2xl shadow-xl p-6">
            <h2 class="text-xl font-bold text-gray-800 mb-4">Recent Activity</h2>
            <div class="space-y-3">
              <div
                v-for="(activity, i) in activities"
                :key="i"
                class="flex items-center justify-between p-4 rounded-xl hover:bg-gray-50 transition-colors border border-gray-100"
              >
                <div class="flex items-center gap-3">
                  <div class="w-2 h-2 rounded-full" :class="activity.color"></div>
                  <span class="font-medium text-gray-800">{{ activity.action }}</span>
                </div>
                <span class="text-sm text-gray-500">{{ activity.time }}</span>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="bg-white rounded-2xl shadow-xl p-8 text-center">
          <component
            :is="currentTab.icon"
            class="w-16 h-16 mx-auto text-gray-300 mb-4"
          />
          <h2 class="text-2xl font-bold text-gray-800 mb-2">{{ currentTab.label }} Page</h2>
          <p class="text-gray-500">This section is coming soon!</p>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import {
  HomeIcon,
  BriefcaseIcon,
  AwardIcon,
  FileTextIcon,
  SettingsIcon,
  BellIcon,
  SearchIcon,
  MenuIcon,
  XIcon,
  ChevronDownIcon
} from 'lucide-vue-next'

const sidebarOpen = ref(true)
const activeTab = ref('dashboard')

const navItems = [
  { id: 'dashboard', icon: HomeIcon, label: 'Dashboard', color: 'from-blue-500 to-blue-600' },
  { id: 'skills', icon: BriefcaseIcon, label: 'Skills', color: 'from-purple-500 to-purple-600' },
  { id: 'certifications', icon: AwardIcon, label: 'Certifications', color: 'from-green-500 to-green-600' },
  { id: 'resume', icon: FileTextIcon, label: 'Resume', color: 'from-orange-500 to-orange-600' },
  { id: 'settings', icon: SettingsIcon, label: 'Settings', color: 'from-gray-500 to-gray-600' }
]

const stats = [
  { label: 'Total Skills', value: '24', change: '+3 this month', color: 'bg-gradient-to-br from-blue-500 to-blue-600' },
  { label: 'Certifications', value: '8', change: '+2 this month', color: 'bg-gradient-to-br from-green-500 to-green-600' },
  { label: 'Projects', value: '12', change: '+1 this week', color: 'bg-gradient-to-br from-purple-500 to-purple-600' },
  { label: 'Profile Views', value: '156', change: '+24 this week', color: 'bg-gradient-to-br from-orange-500 to-orange-600' }
]

const activities = [
  { action: 'Completed Python Certification', time: '2 hours ago', color: 'bg-green-500' },
  { action: 'Updated Resume', time: '1 day ago', color: 'bg-blue-500' },
  { action: 'Added new skill: React', time: '3 days ago', color: 'bg-purple-500' }
]

const currentTab = computed(() => navItems.find(i => i.id === activeTab.value))
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fadeIn {
  animation: fadeIn 0.4s ease-in-out;
}
</style>
