<template>
  <div class="min-h-screen bg-[#f8fafc] flex flex-col justify-center py-2 sm:py-3 px-3 font-sans antialiased selection:bg-[#ED1D24] selection:text-white">
    <!-- Centered Card Container -->
    <div class="max-w-[430px] w-full mx-auto my-auto">
      <!-- StandardTouch Brand Logo & Header -->
      <div class="text-center mb-2">
        <div class="inline-flex items-center justify-center mb-1">
          <StandardTouchIcon customClass="h-9 w-9 shadow-xs" />
        </div>
        <h1 class="text-lg font-extrabold font-heading tracking-tight text-black leading-tight mb-0.5">
          <span class="text-[#ED1D24]">Standard</span><span> Touch Helpdesk Portal</span>
        </h1>
        <p class="text-[11px] text-[#818285] font-semibold tracking-wide">
          Support &amp; Customer Portal
        </p>
      </div>

      <!-- Main Form Card with Visible Stone Grey Border -->
      <div class="bg-white rounded-xl py-3.5 px-5 sm:px-6 card-bordered shadow-md">
        <!-- Segmented Mode Toggle Tabs -->
        <div class="grid grid-cols-2 gap-1 p-0.5 bg-slate-100 rounded-lg mb-2.5 border border-slate-200">
          <button
            type="button"
            @click="setMode('signup')"
            :class="[
              'py-1 text-xs font-bold rounded-md transition-all cursor-pointer font-heading',
              mode === 'signup'
                ? 'bg-white text-black shadow-xs border border-slate-200'
                : 'text-[#818285] hover:text-black'
            ]"
          >
            Create Account
          </button>
          <button
            type="button"
            @click="setMode('signin')"
            :class="[
              'py-1 text-xs font-bold rounded-md transition-all cursor-pointer font-heading',
              mode === 'signin'
                ? 'bg-white text-black shadow-xs border border-slate-200'
                : 'text-[#818285] hover:text-black'
            ]"
          >
            Sign In
          </button>
        </div>

        <div class="mb-2">
          <h2 class="text-sm font-extrabold text-black font-heading tracking-tight">
            {{ mode === 'signup' ? "Create your client account" : mode === 'signin' ? "Welcome back" : "Reset your password" }}
          </h2>
          <p class="text-[10.5px] text-[#818285] mt-0.5 font-medium leading-tight">
            {{
              mode === 'signup'
                ? "Sign up to track and submit support tickets directly."
                : mode === 'signin'
                ? "Enter your credentials to access your support dashboard."
                : "Enter your work email address to receive password reset instructions."
            }}
          </p>
        </div>

        <!-- Error Notification -->
        <div
          v-if="errorMessage"
          class="mb-2 rounded-lg bg-red-50 p-2 border border-red-200 text-xs text-[#ED1D24] font-medium flex items-start space-x-1.5"
        >
          <svg class="h-3.5 w-3.5 text-[#ED1D24] shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" />
            <line x1="12" y1="8" x2="12" y2="12" />
            <line x1="12" y1="16" x2="12.01" y2="16" />
          </svg>
          <span>{{ errorMessage }}</span>
        </div>

        <!-- Signup Form -->
        <form v-if="mode === 'signup'" class="space-y-1.5" @submit.prevent="handleSignup">
          <!-- Full Name -->
          <div>
            <label for="full_name" class="block text-[10px] font-bold text-black uppercase tracking-wider mb-0.5 font-heading">
              Full Name <span class="text-[#ED1D24]">*</span>
            </label>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2.5 text-[#818285]">
                <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                  <circle cx="12" cy="7" r="4" />
                </svg>
              </div>
              <input
                id="full_name"
                v-model="form.fullName"
                type="text"
                required
                autocomplete="name"
                placeholder="John Doe"
                class="custom-input pl-8 pr-3 py-1 text-xs"
              />
            </div>
          </div>

          <!-- Work Email -->
          <div>
            <label for="email" class="block text-[10px] font-bold text-black uppercase tracking-wider mb-0.5 font-heading">
              Work Email <span class="text-[#ED1D24]">*</span>
            </label>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2.5 text-[#818285]">
                <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                  <polyline points="22,6 12,13 2,6" />
                </svg>
              </div>
              <input
                id="email"
                v-model="form.email"
                type="email"
                required
                autocomplete="email"
                placeholder="you@company.com"
                class="custom-input pl-8 pr-3 py-1 text-xs"
              />
            </div>
          </div>

          <!-- Organization / Company -->
          <div>
            <label for="company_name" class="block text-[10px] font-bold text-black uppercase tracking-wider mb-0.5 font-heading">
              Organization / Company <span class="text-[#ED1D24]">*</span>
            </label>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2.5 text-[#818285]">
                <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path d="M3 21h18" />
                  <path d="M9 8h1" />
                  <path d="M9 12h1" />
                  <path d="M9 16h1" />
                  <path d="M14 8h1" />
                  <path d="M14 12h1" />
                  <path d="M14 16h1" />
                  <path d="M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16" />
                </svg>
              </div>
              <input
                id="company_name"
                v-model="form.companyName"
                type="text"
                required
                autocomplete="organization"
                placeholder="Your company name"
                class="custom-input pl-8 pr-3 py-1 text-xs"
              />
            </div>
          </div>

          <!-- Password -->
          <div>
            <label for="password" class="block text-[10px] font-bold text-black uppercase tracking-wider mb-0.5 font-heading">
              Password <span class="text-[#ED1D24]">*</span>
            </label>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2.5 text-[#818285]">
                <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                </svg>
              </div>
              <input
                id="password"
                v-model="form.password"
                :type="showPassword ? 'text' : 'password'"
                required
                autocomplete="new-password"
                placeholder="At least 6 characters"
                class="custom-input pl-8 pr-8 py-1 text-xs"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 flex items-center pr-2.5 text-[#818285] hover:text-black focus:outline-none cursor-pointer bg-transparent border-0"
              >
                <svg v-if="!showPassword" class="h-3.5 w-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8z" />
                  <circle cx="12" cy="12" r="3" />
                </svg>
                <svg v-else class="h-3.5 w-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
                  <line x1="1" y1="1" x2="23" y2="23" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Terms Checkbox -->
          <div class="flex items-center pt-0.5">
            <input
              id="agree_terms"
              v-model="form.agreeTerms"
              type="checkbox"
              required
              class="custom-checkbox h-3.5 w-3.5 cursor-pointer"
            />
            <label for="agree_terms" class="ml-2 block text-[10.5px] text-[#818285] cursor-pointer select-none font-medium">
              I agree to the <a href="#" class="underline text-black hover:text-[#ED1D24]">Terms of Service</a> and
              <a href="#" class="underline text-black hover:text-[#ED1D24]">Privacy Policy</a>
            </label>
          </div>

          <!-- Submit Button in Brand Red #ED1D24 -->
          <button
            type="submit"
            :disabled="loading"
            class="custom-button mt-1.5 w-full flex items-center justify-center rounded-lg px-3 py-2 text-xs font-bold shadow-xs disabled:opacity-60 cursor-pointer border-0 font-heading"
          >
            <svg
              v-if="loading"
              class="mr-1.5 h-3.5 w-3.5 animate-spin text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span>{{ loading ? "Creating Account..." : "Create Account" }}</span>
            <span v-if="!loading" class="ml-1" aria-hidden="true">&rarr;</span>
          </button>
        </form>

        <!-- Signin Form -->
        <form v-else-if="mode === 'signin'" class="space-y-1.5" @submit.prevent="handleSignin">
          <!-- Work Email / Username -->
          <div>
            <label for="signin_email" class="block text-[10px] font-bold text-black uppercase tracking-wider mb-0.5 font-heading">
              Work Email / Username <span class="text-[#ED1D24]">*</span>
            </label>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2.5 text-[#818285]">
                <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                  <polyline points="22,6 12,13 2,6" />
                </svg>
              </div>
              <input
                id="signin_email"
                v-model="signinForm.email"
                type="text"
                required
                autocomplete="username"
                placeholder="you@company.com"
                class="custom-input pl-8 pr-3 py-1 text-xs"
              />
            </div>
          </div>

          <!-- Password -->
          <div>
            <div class="flex items-center justify-between mb-0.5">
              <label for="signin_password" class="block text-[10px] font-bold text-black uppercase tracking-wider font-heading">
                Password <span class="text-[#ED1D24]">*</span>
              </label>
            </div>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2.5 text-[#818285]">
                <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                </svg>
              </div>
              <input
                id="signin_password"
                v-model="signinForm.password"
                :type="showPassword ? 'text' : 'password'"
                required
                autocomplete="current-password"
                placeholder="Enter your password"
                class="custom-input pl-8 pr-8 py-1 text-xs"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 flex items-center pr-2.5 text-[#818285] hover:text-black focus:outline-none cursor-pointer bg-transparent border-0"
              >
                <svg v-if="!showPassword" class="h-3.5 w-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8z" />
                  <circle cx="12" cy="12" r="3" />
                </svg>
                <svg v-else class="h-3.5 w-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
                  <line x1="1" y1="1" x2="23" y2="23" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between pt-0.5">
            <div class="flex items-center">
              <input
                id="remember_me"
                v-model="signinForm.rememberMe"
                type="checkbox"
                class="custom-checkbox h-3.5 w-3.5 cursor-pointer"
              />
              <label for="remember_me" class="ml-2 block text-[10.5px] text-[#818285] cursor-pointer select-none font-medium">
                Remember me
              </label>
            </div>
            <button
              type="button"
              @click="setMode('forgot')"
              class="text-[10.5px] text-[#818285] hover:text-[#ED1D24] underline cursor-pointer bg-transparent border-0 font-medium"
            >
              Forgot password?
            </button>
          </div>

          <!-- Submit Button in Brand Red #ED1D24 -->
          <button
            type="submit"
            :disabled="loading"
            class="custom-button mt-1.5 w-full flex items-center justify-center rounded-lg px-3 py-2 text-xs font-bold shadow-xs disabled:opacity-60 cursor-pointer border-0 font-heading"
          >
            <svg
              v-if="loading"
              class="mr-1.5 h-3.5 w-3.5 animate-spin text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span>{{ loading ? "Signing In..." : "Sign In" }}</span>
            <span v-if="!loading" class="ml-1" aria-hidden="true">&rarr;</span>
          </button>
        </form>

        <!-- Forgot Password Form -->
        <form v-else-if="mode === 'forgot'" class="space-y-2" @submit.prevent="handleForgotPassword">
          <div v-if="forgotSuccess" class="rounded-lg bg-emerald-50 p-2.5 border border-emerald-200 text-xs text-emerald-800 font-medium flex items-start space-x-1.5">
            <svg class="h-4 w-4 text-emerald-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span>If an account exists for this email, password reset instructions have been sent. Please check your inbox.</span>
          </div>

          <div v-else class="space-y-1.5">
            <div>
              <label for="forgot_email" class="block text-[10px] font-bold text-black uppercase tracking-wider mb-0.5 font-heading">
                Work Email <span class="text-[#ED1D24]">*</span>
              </label>
              <div class="relative">
                <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2.5 text-[#818285]">
                  <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                    <polyline points="22,6 12,13 2,6" />
                  </svg>
                </div>
                <input
                  id="forgot_email"
                  v-model="forgotEmail"
                  type="email"
                  required
                  autocomplete="email"
                  placeholder="you@company.com"
                  class="custom-input pl-8 pr-3 py-1 text-xs"
                />
              </div>
            </div>

            <button
              type="submit"
              :disabled="loading"
              class="custom-button mt-1.5 w-full flex items-center justify-center rounded-lg px-3 py-2 text-xs font-bold shadow-xs disabled:opacity-60 cursor-pointer border-0 font-heading"
            >
              <svg
                v-if="loading"
                class="mr-1.5 h-3.5 w-3.5 animate-spin text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>{{ loading ? "Sending Link..." : "Send Reset Link" }}</span>
            </button>
          </div>

          <div class="text-center pt-1">
            <button
              type="button"
              @click="setMode('signin')"
              class="text-xs text-[#818285] hover:text-black underline cursor-pointer bg-transparent border-0 font-medium"
            >
              &larr; Back to Sign In
            </button>
          </div>
        </form>

        <!-- Social Logins (Google, Apple, etc.) -->
        <div v-if="mode !== 'forgot'" class="mt-2.5">
          <div class="relative my-2">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-slate-200"></div>
            </div>
            <div class="relative flex justify-center text-[10px] text-[#818285]">
              <span class="bg-white px-2 font-medium">or continue with</span>
            </div>
          </div>

          <!-- If Frappe has dynamic OAuth configured -->
          <div v-if="oauthProviders.length" class="space-y-1.5">
            <a
              v-for="provider in oauthProviders"
              :key="provider.name"
              :href="provider.auth_url"
              class="social-button w-full flex items-center justify-center px-3 py-1.5 text-xs font-semibold shadow-2xs cursor-pointer text-black hover:text-[#ED1D24] no-underline font-heading"
            >
              <span v-if="provider.icon" v-html="provider.icon" class="mr-2 flex items-center shrink-0"></span>
              <span>Continue with {{ provider.provider_name || provider.name }}</span>
            </a>
          </div>

          <!-- Default Google & Apple buttons -->
          <div v-else class="space-y-1.5">
            <button
              type="button"
              @click="handleSocialLogin('google')"
              class="social-button w-full flex items-center justify-center px-3 py-1.5 text-xs font-semibold shadow-2xs cursor-pointer text-black hover:text-[#ED1D24] font-heading"
            >
              <svg class="h-3.5 w-3.5 mr-2 shrink-0" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
              </svg>
              <span>Continue with Google</span>
            </button>

            <button
              type="button"
              @click="handleSocialLogin('apple')"
              class="social-button w-full flex items-center justify-center px-3 py-1.5 text-xs font-semibold shadow-2xs cursor-pointer text-black hover:text-[#ED1D24] font-heading"
            >
              <svg class="h-3.5 w-3.5 mr-2 shrink-0 fill-current text-black" viewBox="0 0 24 24">
                <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.85c.64-.78 1.08-1.86.96-2.95-1 .04-2.14.65-2.82 1.45-.6.69-1.12 1.79-.98 2.86 1.12.09 2.2-.58 2.84-1.36z"/>
              </svg>
              <span>Continue with Apple</span>
            </button>
          </div>
        </div>

        <!-- Card Footer -->
        <div class="mt-2.5 pt-2 border-t border-slate-100 flex items-center justify-between text-[11px] text-[#818285]">
          <div class="flex items-center space-x-1">
            <svg class="h-3 w-3 text-[#818285]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
              <path d="M9 12l2 2 4-4" />
            </svg>
            <span>StandardTouch Secure Encryption</span>
          </div>
          <a href="/login?redirect-to=/app" class="text-[11px] text-[#818285] hover:text-[#ED1D24] underline">
            Staff / Desk Login &rarr;
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref, onMounted } from "vue";
import { call } from "frappe-ui";
import StandardTouchLogo from "@/assets/logos/StandardTouchLogo.vue";
import StandardTouchIcon from "@/assets/logos/StandardTouchIcon.vue";

const props = withDefaults(
  defineProps<{
    defaultMode?: "signup" | "signin" | "forgot";
  }>(),
  {
    defaultMode: "signup",
  }
);

const mode = ref<"signup" | "signin" | "forgot">(
  props.defaultMode === "signin" ? "signin" : props.defaultMode === "forgot" ? "forgot" : "signup"
);
const oauthProviders = ref<any[]>([]);

onMounted(async () => {
  if (window.location.pathname.endsWith("/forgot-password")) {
    mode.value = "forgot";
  } else if (window.location.pathname.endsWith("/login")) {
    mode.value = "signin";
  }
  try {
    const res = await call("helpdesk.api.auth.oauth_providers");
    if (Array.isArray(res)) {
      oauthProviders.value = res;
    }
  } catch (e) {
    // ignore
  }
});

function setMode(newMode: "signup" | "signin" | "forgot") {
  errorMessage.value = "";
  forgotSuccess.value = false;
  mode.value = newMode;
  if (newMode === "signin") {
    window.history.replaceState(null, "", "/helpdesk/login");
  } else if (newMode === "forgot") {
    window.history.replaceState(null, "", "/helpdesk/forgot-password");
  } else {
    window.history.replaceState(null, "", "/helpdesk/signup");
  }
}

// Signup Form State
const form = reactive({
  fullName: "",
  email: "",
  companyName: "",
  password: "",
  agreeTerms: true,
});

// Signin Form State
const signinForm = reactive({
  email: "",
  password: "",
  rememberMe: true,
});

const showPassword = ref(false);
const loading = ref(false);
const errorMessage = ref("");

async function handleSignup() {
  errorMessage.value = "";
  if (
    !form.fullName.trim() ||
    !form.email.trim() ||
    !form.companyName.trim() ||
    !form.password.trim()
  ) {
    errorMessage.value = "Please fill in all required fields.";
    return;
  }

  if (form.password.length < 6) {
    errorMessage.value = "Password must be at least 6 characters long.";
    return;
  }

  if (!form.agreeTerms) {
    errorMessage.value = "Please agree to the Terms of Service and Privacy Policy.";
    return;
  }

  loading.value = true;
  try {
    const res = await call("helpdesk.api.account.register_portal_user", {
      full_name: form.fullName.trim(),
      email: form.email.trim(),
      company_name: form.companyName.trim(),
      password: form.password,
    });

    if (res && res.status === "success") {
      window.location.href = res.redirect_to || "/helpdesk/my-tickets";
    } else {
      window.location.href = "/helpdesk/my-tickets";
    }
  } catch (error: any) {
    loading.value = false;
    let message = "Failed to create account. Please try again.";
    if (error.messages && error.messages.length) {
      message = error.messages.join(", ");
    } else if (error.message) {
      message = error.message;
    }
    errorMessage.value = message;
  }
}

const forgotEmail = ref("");
const forgotSuccess = ref(false);

async function handleForgotPassword() {
  errorMessage.value = "";
  if (!forgotEmail.value || !forgotEmail.value.trim()) {
    errorMessage.value = "Please enter your work email address.";
    return;
  }
  loading.value = true;
  try {
    await call("frappe.core.doctype.user.user.reset_password", {
      user: forgotEmail.value.trim(),
    });
    forgotSuccess.value = true;
  } catch (error: any) {
    let message = "Could not send password reset instructions.";
    if (error.messages && error.messages.length) {
      message = error.messages.join(", ");
    } else if (error.message) {
      message = error.message;
    }
    errorMessage.value = message;
  } finally {
    loading.value = false;
  }
}

async function handleSignin() {
  errorMessage.value = "";
  if (!signinForm.email.trim() || !signinForm.password.trim()) {
    errorMessage.value = "Please enter your email and password.";
    return;
  }

  loading.value = true;
  try {
    await call("login", {
      usr: signinForm.email.trim(),
      pwd: signinForm.password,
    });

    try {
      const redirectUrl = await call("helpdesk.api.auth.get_post_login_redirect");
      window.location.href = redirectUrl || "/helpdesk/my-tickets";
    } catch {
      window.location.href = "/helpdesk/my-tickets";
    }
  } catch (error: any) {
    loading.value = false;
    let message = "Invalid email or password.";
    if (error.messages && error.messages.length) {
      message = error.messages.join(", ");
    } else if (error.message) {
      message = error.message;
    }
    errorMessage.value = message;
  }
}

async function handleSocialLogin(provider: string) {
  errorMessage.value = "";
  try {
    const res = await call("helpdesk.api.auth.oauth_providers");
    const match =
      res &&
      res.find(
        (p: any) =>
          (p.name && p.name.toLowerCase() === provider.toLowerCase()) ||
          (p.provider_name && p.provider_name.toLowerCase() === provider.toLowerCase())
      );
    if (match && match.auth_url) {
      window.location.href = match.auth_url;
      return;
    }
  } catch (e) {
    // ignore
  }

  const name = provider.charAt(0).toUpperCase() + provider.slice(1);
  errorMessage.value = `${name} login is not configured on this site. An administrator must configure ${name} OAuth credentials under 'Social Login Key' in Frappe Desk.`;
}
</script>

<style scoped>
.font-heading {
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}

.card-bordered {
  border: 1px solid #e2e8f0 !important;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.03) !important;
}

.custom-input {
  display: block;
  width: 100%;
  font-family: 'Montserrat', sans-serif !important;
  border: 1px solid #d1d5db !important;
  border-radius: 0.375rem !important;
  background-color: #ffffff !important;
  color: #111827 !important;
  font-size: 0.75rem !important;
  line-height: 1rem !important;
  padding-top: 0.375rem !important;
  padding-bottom: 0.375rem !important;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.02) !important;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out !important;
}

.custom-input:hover {
  border-color: #9ca3af !important;
}

.custom-input:focus {
  border-color: #ED1D24 !important; /* Brand Red #ED1D24 from brand kit */
  box-shadow: 0 0 0 2.5px rgba(237, 29, 36, 0.12) !important;
  outline: none !important;
}

.custom-input::placeholder {
  color: #9ca3af !important;
}

.custom-button {
  background-color: #ED1D24 !important; /* Brand Red #ED1D24 */
  color: #ffffff !important;
  transition: all 0.15s ease-in-out !important;
}

.custom-button:hover:not(:disabled) {
  background-color: #d0171d !important; /* Darker red */
}

.custom-button:active:not(:disabled) {
  background-color: #b81016 !important;
}

.social-button {
  border: 1px solid #e2e8f0 !important;
  background-color: #ffffff !important;
  color: #1f2937 !important;
  border-radius: 0.5rem !important;
  transition: all 0.15s ease-in-out !important;
}

.social-button:hover {
  border-color: #cbd5e1 !important;
  background-color: #f8fafc !important;
}

.custom-checkbox {
  border: 1px solid #d1d5db !important;
  border-radius: 0.25rem !important;
  accent-color: #ED1D24 !important; /* Brand Red accent */
}
</style>
