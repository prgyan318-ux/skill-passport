<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-100 via-white to-purple-100">
    <!-- Card -->
    <div class="w-full max-w-md bg-white/80 backdrop-blur-xl shadow-xl rounded-2xl p-8 text-center border border-gray-100">
      <!-- Title -->
      <h1 class="text-2xl font-bold text-gray-800 mb-2">Welcome to Skill Passport</h1>
      <p class="text-gray-500 mb-6">Sign in to continue your journey</p>

      <!-- Buttons -->
      <div class="space-y-3">
        <!-- Google -->
        <button
          class="w-full flex items-center justify-center gap-3 bg-white border border-gray-200 rounded-lg py-2.5 hover:bg-gray-50 transition"
        >
          <img src="https://www.svgrepo.com/show/475656/google-color.svg" class="w-5 h-5" alt="Google" />
          <span class="font-medium text-gray-700">Sign in with Google</span>
        </button>

        <!-- LinkedIn -->
        <button
          class="w-full flex items-center justify-center gap-3 bg-[#0077b5] text-white rounded-lg py-2.5 hover:bg-[#006097] transition"
        >
          <img src="https://www.svgrepo.com/show/448234/linkedin.svg" class="w-5 h-5 invert" alt="LinkedIn" />
          <span class="font-medium">Sign in with LinkedIn</span>
        </button>

        <!-- Email -->
        <button
          class="w-full flex items-center justify-center gap-3 bg-gray-800 text-white rounded-lg py-2.5 hover:bg-gray-900 transition"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12H8m8 0l-4-4m0 8l4-4m-4 4V8" />
          </svg>
          <span class="font-medium">Sign in with Email</span>
        </button>
      </div>

      <!-- Divider -->
      <div class="flex items-center gap-2 my-6">
        <div class="flex-grow h-px bg-gray-200"></div>
        <span class="text-sm text-gray-400">or</span>
        <div class="flex-grow h-px bg-gray-200"></div>
      </div>

      <!-- Register link -->
      <p class="text-gray-500 text-sm">
        Don’t have an account?
        <a href="#" class="text-blue-600 font-medium hover:underline">Create one</a>
      </p>
    </div>

    <!-- Footer -->
    <p class="mt-6 text-sm text-gray-400">&copy; 2025 Skill Passport. All rights reserved.</p>
  </div>
</template>

<script setup>
// You can later add router navigation or Google OAuth here
</script>
 