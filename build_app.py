import json

with open('/Users/macbook/Documents/antigravity/pocketmon/pokemon_data.json', 'r', encoding='utf-8') as f:
    pokemon_data = json.load(f)

# Initial students with default passwords and daily checkin date tracking
initial_students = [
    {"id": 1, "number": 1, "name": "강해나", "password": "0001", "count": 0, "happy": 150, "pendingBalls": 1, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 2, "number": 2, "name": "김나연", "password": "0002", "count": 0, "happy": 150, "pendingBalls": 1, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 3, "number": 3, "name": "김인애", "password": "0003", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 4, "number": 4, "name": "김제은", "password": "0004", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 5, "number": 5, "name": "김태호", "password": "0005", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 6, "number": 6, "name": "박민하", "password": "0006", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 7, "number": 7, "name": "안세연", "password": "0007", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 8, "number": 8, "name": "염하준", "password": "0008", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 9, "number": 9, "name": "오진욱", "password": "0009", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 10, "number": 10, "name": "이규림", "password": "0010", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 11, "number": 11, "name": "이성빈", "password": "0011", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 12, "number": 12, "name": "정하람", "password": "0012", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 13, "number": 13, "name": "조윤아", "password": "0013", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 14, "number": 14, "name": "이지후", "password": "0014", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 15, "number": 15, "name": "한태우", "password": "0015", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
    {"id": 16, "number": 16, "name": "허소율", "password": "0016", "count": 0, "happy": 150, "pendingBalls": 0, "representativePokeId": None, "todayLog": None, "lastAttendance": "", "trainedToday": False, "collected": {}},
]

html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>우리 반 포켓몬 발표 도감</title>
  <!-- Google Fonts: Jua & Noto Sans KR -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
  <!-- Firebase Cloud Sync (Free Realtime Firestore) -->
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>
  <script src="firebase_config.js"></script>

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            jua: ['Jua', 'sans-serif'],
            sans: ['Noto Sans KR', 'sans-serif'],
          },
          keyframes: {
            ballWiggle: {
              '0%, 100%': { transform: 'rotate(0deg)' },
              '20%': { transform: 'rotate(-25deg)' },
              '40%': { transform: 'rotate(25deg)' },
              '60%': { transform: 'rotate(-15deg)' },
              '80%': { transform: 'rotate(15deg)' },
            },
            ballBounce: {
              '0%, 100%': { transform: 'translateY(0)' },
              '50%': { transform: 'translateY(-20px)' },
            },
            cardPop: {
              '0%': { transform: 'scale(0.7) translateY(40px)', opacity: '0' },
              '70%': { transform: 'scale(1.04) translateY(-5px)', opacity: '1' },
              '100%': { transform: 'scale(1) translateY(0)', opacity: '1' },
            },
          },
          animation: {
            'ball-wiggle': 'ballWiggle 0.6s ease-in-out infinite',
            'ball-bounce': 'ballBounce 0.8s ease-in-out infinite',
            'card-pop': 'cardPop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards',
          }
        }
      }
    }
  </script>

  <style>
    body {
      font-family: 'Noto Sans KR', sans-serif;
      user-select: none;
      -webkit-user-select: none;
    }
    .font-jua {
      font-family: 'Jua', sans-serif;
    }
    .pokeball-btn {
      background: linear-gradient(to bottom, #ef4444 50%, #ffffff 50%);
      position: relative;
      border: 3px solid #1f2937;
    }
    .pokeball-btn::before {
      content: '';
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 6px;
      background: #1f2937;
      transform: translateY(-50%);
    }
    .pokeball-btn::after {
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      width: 22px;
      height: 22px;
      background: #ffffff;
      border: 4px solid #1f2937;
      border-radius: 50%;
      transform: translate(-50%, -50%);
      box-shadow: 0 0 0 2px rgba(0,0,0,0.1);
    }

    .mini-ball {
      width: 18px;
      height: 18px;
      background: linear-gradient(to bottom, #ef4444 50%, #ffffff 50%);
      position: relative;
      border: 2px solid #1f2937;
      border-radius: 50%;
      display: inline-block;
      vertical-align: middle;
    }
    .mini-ball::before {
      content: '';
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      height: 2px;
      background: #1f2937;
      transform: translateY(-50%);
    }
    .mini-ball::after {
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      width: 6px;
      height: 6px;
      background: #ffffff;
      border: 1.5px solid #1f2937;
      border-radius: 50%;
      transform: translate(-50%, -50%);
    }

    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(0, 0, 0, 0.1);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.3);
      border-radius: 4px;
    }

    .holo-card {
      background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 50%, #fef08a 100%);
      box-shadow: 0 20px 40px -15px rgba(0,0,0,0.5), 0 0 25px rgba(250, 204, 21, 0.4);
    }
    .holo-card-rare {
      background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 50%, #ddd6fe 100%);
      box-shadow: 0 20px 40px -15px rgba(109, 40, 217, 0.5), 0 0 25px rgba(167, 139, 250, 0.5);
    }
    .holo-card-legendary {
      background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 30%, #fed7aa 70%, #fde047 100%);
      box-shadow: 0 25px 50px -12px rgba(217, 119, 6, 0.6), 0 0 35px rgba(251, 191, 36, 0.8);
      position: relative;
    }
    .holo-card-legendary::before {
      content: '';
      position: absolute;
      inset: -2px;
      border-radius: inherit;
      padding: 3px;
      background: linear-gradient(45deg, #f59e0b, #ec4899, #8b5cf6, #3b82f6, #10b981, #f59e0b);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: rotateBorder 4s linear infinite;
    }
    @keyframes rotateBorder {
      0% { filter: hue-rotate(0deg); }
      100% { filter: hue-rotate(360deg); }
    }
  </style>
</head>
<body class="bg-[#0f172a] text-slate-100 min-h-screen flex flex-col selection:bg-amber-400 selection:text-slate-900">

  <!-- Toast Notification Alert -->
  <div id="toastAlert" class="fixed top-5 left-1/2 -translate-x-1/2 z-50 px-5 py-3 rounded-2xl bg-slate-900/95 border-2 border-emerald-400 text-white font-jua text-sm shadow-2xl transition-all duration-300 opacity-0 pointer-events-none transform -translate-y-4 flex items-center gap-2.5">
    <span class="mini-ball"></span>
    <span id="toastMessage">안내 메시지</span>
  </div>

  <!-- ==================== 1. LOGIN SCREEN ==================== -->
  <div id="loginScreen" class="fixed inset-0 z-40 bg-[#0f172a] flex flex-col items-center justify-center p-4">
    <div class="w-full max-w-md bg-[#1e293b] border-2 border-slate-700 rounded-3xl p-6 sm:p-8 shadow-2xl flex flex-col items-center animate-card-pop relative">
      <div class="w-20 h-20 rounded-full pokeball-btn shadow-xl animate-bounce mb-4 flex-shrink-0 cursor-pointer" onclick="soundManager.playFanfare()"></div>
      <h1 class="text-2xl sm:text-3xl font-jua text-amber-300 mb-1 text-center">우리 반 포켓몬 발표 도감</h1>
      <p class="text-xs text-slate-400 mb-6 text-center">로그인 유형을 선택해주세요</p>

      <div class="grid grid-cols-2 gap-2 w-full p-1 bg-slate-900 rounded-2xl border border-slate-700/80 mb-6">
        <button id="tabStudentBtn" onclick="switchLoginTab('student')" class="py-2.5 rounded-xl font-jua text-sm transition bg-emerald-500 text-slate-950 font-bold shadow">
          🎒 학생 로그인
        </button>
        <button id="tabTeacherBtn" onclick="switchLoginTab('teacher')" class="py-2.5 rounded-xl font-jua text-sm transition text-slate-300 hover:text-white">
          👨‍🏫 선생님 로그인
        </button>
      </div>

      <!-- Student Login Form -->
      <form id="studentLoginForm" onsubmit="handleStudentLogin(event)" class="w-full flex flex-col gap-4">
        <div>
          <label class="block text-xs font-bold text-slate-300 mb-1.5">내 이름 선택:</label>
          <select id="loginStudentSelect" class="w-full p-3 rounded-xl border-2 border-slate-600 bg-slate-900 text-white font-jua text-base focus:outline-none focus:border-emerald-400">
          </select>
        </div>

        <div>
          <label class="block text-xs font-bold text-slate-300 mb-1.5">비밀번호 (PIN 번호):</label>
          <input type="password" id="loginStudentPw" placeholder="비밀번호 입력 (예: 0001)" class="w-full p-3 rounded-xl border-2 border-slate-600 bg-slate-900 text-white font-mono text-base focus:outline-none focus:border-emerald-400 text-center tracking-widest" required autocomplete="off" />
          <p class="text-[11px] text-slate-400 mt-1.5 text-center">💡 기본 비밀번호: 학생 번호 4자리 (예: 1번은 <span class="text-amber-300 font-mono">0001</span>)</p>
        </div>

        <button type="submit" class="w-full mt-2 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 active:scale-95 text-slate-950 font-jua text-base shadow-lg transition flex items-center justify-center gap-2">
          <span>🚀</span>
          <span>내 포켓몬 세상으로 들어가기</span>
        </button>
      </form>

      <!-- Teacher Login Form -->
      <form id="teacherLoginForm" onsubmit="handleTeacherLogin(event)" class="w-full flex flex-col gap-4 hidden">
        <div>
          <label class="block text-xs font-bold text-slate-300 mb-1.5">선생님 비밀번호:</label>
          <input type="password" id="loginTeacherPw" placeholder="선생님 비밀번호 입력" class="w-full p-3 rounded-xl border-2 border-slate-600 bg-slate-900 text-white font-mono text-base focus:outline-none focus:border-amber-400 text-center tracking-widest" required autocomplete="off" />
          <p class="text-[11px] text-slate-400 mt-1.5 text-center">💡 기본 비밀번호: <span class="text-amber-300 font-mono">1234</span></p>
        </div>

        <button type="submit" class="w-full mt-2 py-3.5 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 active:scale-95 text-slate-950 font-jua text-base shadow-lg transition flex items-center justify-center gap-2">
          <span>👨‍🏫</span>
          <span>선생님 관리 대시보드 열기</span>
        </button>
      </form>
    </div>
  </div>

  <!-- ==================== 2. TEACHER VIEW ==================== -->
  <div id="teacherView" class="hidden flex-1 flex flex-col">
    <!-- Top Navigation / Header -->
    <header class="bg-[#1e293b]/90 backdrop-blur border-b border-slate-700/60 sticky top-0 z-30 px-4 py-3 shadow-lg">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full pokeball-btn shadow-md flex-shrink-0 animate-bounce cursor-pointer" onclick="soundManager.playFanfare()" title="포켓볼 클릭!"></div>
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xs bg-amber-400 text-slate-950 font-bold px-2 py-0.5 rounded-full font-jua">선생님 모드</span>
              <h1 id="headerClassName" class="text-xl sm:text-2xl font-jua text-amber-300 tracking-wide drop-shadow-sm flex items-center gap-2">
                행복한 5학년의 발표 포켓몬
              </h1>
              <button onclick="openClassSettings()" class="text-slate-400 hover:text-amber-300 text-xs transition" title="학급명 변경">
                ✏️
              </button>
            </div>
            <p class="text-xs text-slate-400 font-medium">수업 중 발표 적립 및 발표자 추첨 룰렛</p>
          </div>
        </div>

        <div class="flex items-center gap-2 sm:gap-2.5 flex-wrap">
          <div class="cloud-sync-badge flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-800 border border-slate-700 text-slate-400 text-xs font-jua cursor-pointer transition">
            <span class="w-2 h-2 rounded-full bg-slate-500"></span>
            <span>로컬 모드</span>
          </div>

          <button onclick="openRouletteModal()" class="flex items-center gap-1.5 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 active:scale-95 text-slate-900 font-jua px-3.5 py-2 rounded-xl shadow-md transition text-xs sm:text-sm">
            <span>🎲</span>
            <span>발표자 추첨</span>
          </button>

          <button id="soundToggleBtn" onclick="toggleSound()" class="bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-200 border border-slate-700 p-2 rounded-xl transition shadow text-base" title="소리 켜기/끄기">
            🔊
          </button>

          <button onclick="openManageModal()" class="bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-200 border border-slate-700 px-3 py-2 rounded-xl transition shadow text-xs sm:text-sm font-medium flex items-center gap-1">
            <span>⚙️</span>
            <span class="hidden sm:inline">명단/포인트 규칙</span>
          </button>

          <button onclick="logout()" class="bg-rose-900/40 hover:bg-rose-800/60 border border-rose-700 text-rose-200 px-3 py-2 rounded-xl transition text-xs font-jua">
            로그아웃
          </button>
        </div>
      </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 flex flex-col gap-5">
      <!-- Classroom Guide Banner with Economy Rules -->
      <div class="bg-gradient-to-r from-slate-800 via-slate-800/90 to-slate-800 border border-slate-700/80 p-3.5 sm:p-4 rounded-2xl flex flex-wrap items-center justify-between gap-3 text-xs">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-xl bg-amber-400/20 text-amber-300 flex items-center justify-center text-lg flex-shrink-0">
            🪙
          </div>
          <div class="text-slate-300 leading-snug">
            <p class="font-bold text-white mb-0.5">해피 포인트 & 볼 교환 규칙</p>
            <p class="text-slate-400">
              • 매일 출석: <span class="text-amber-300 font-bold">+20 해피</span> &nbsp;|&nbsp; 
              • 발표 적립: <span class="text-amber-300 font-bold">+15 해피</span> &nbsp;|&nbsp; 
              • <span class="text-rose-400 font-bold">100 해피</span> 모으면 <span class="text-emerald-400 font-bold">추가 몬스터볼 교환</span> 가능!
            </p>
          </div>
        </div>
        <div class="flex items-center gap-3 bg-slate-900/80 px-3.5 py-1.5 rounded-xl border border-slate-700 text-xs">
          <span class="text-amber-400 font-bold">오늘 발표: <span id="statTodayCount" class="text-white">0회</span></span>
          <span class="text-slate-600">|</span>
          <span class="text-emerald-400 font-bold">도감: <span id="statTotalCollected" class="text-white">0/152종</span></span>
          <span class="text-slate-600">|</span>
          <span class="text-rose-400 font-bold">미개봉 볼: <span id="statPendingBallsTotal" class="text-white font-bold">0개</span></span>
        </div>
      </div>

      <!-- Student Cards Grid -->
      <section>
        <div class="flex items-center justify-between mb-3">
          <div class="flex items-center gap-2">
            <span class="text-lg">🎒</span>
            <h2 class="text-lg sm:text-xl font-jua text-slate-200">우리 반 학생 명단 (<span id="studentTotalCount">16</span>명)</h2>
          </div>
          <span class="text-xs text-slate-400">발표한 학생의 <span class="text-amber-300 font-bold">[+1 볼 저장]</span>을 누르면 볼과 해피(+15)가 적립됩니다.</span>
        </div>

        <div id="studentGrid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3 sm:gap-4">
        </div>
      </section>
    </main>

    <footer class="mt-auto py-4 text-center text-xs text-slate-500 border-t border-slate-800/80">
      <p>우리 반 포켓몬 발표 도감 • 선생님 관리 모드</p>
    </footer>
  </div>

  <!-- ==================== 3. STUDENT PERSONAL VIEW ==================== -->
  <div id="studentView" class="hidden flex-1 flex flex-col">
    <!-- Header -->
    <header class="bg-[#1e293b]/90 backdrop-blur border-b border-slate-700/60 sticky top-0 z-30 px-4 py-3 shadow-lg">
      <div class="max-w-4xl mx-auto flex items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full pokeball-btn shadow-md flex-shrink-0 animate-bounce cursor-pointer" onclick="soundManager.playFanfare()"></div>
          <div>
            <div class="flex items-center gap-2">
              <span id="studentViewNumberBadge" class="text-xs bg-emerald-500 text-slate-950 font-bold px-2 py-0.5 rounded-full font-jua">1번</span>
              <h1 id="studentViewName" class="text-xl sm:text-2xl font-jua text-amber-300">
                강해나의 포켓몬 연구실
              </h1>
            </div>
            <p class="text-xs text-slate-400">내 포켓몬을 뽑고 레벨업하며 도감을 채워요! ✨</p>
          </div>
        </div>

        <div class="flex items-center gap-2">
          <div class="cloud-sync-badge flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-800 border border-slate-700 text-slate-400 text-xs font-jua cursor-pointer transition">
            <span class="w-2 h-2 rounded-full bg-slate-500"></span>
            <span>로컬 모드</span>
          </div>
          <button onclick="toggleSound()" class="bg-slate-800 hover:bg-slate-700 p-2 rounded-xl text-base border border-slate-700 transition">
            🔊
          </button>
          <button onclick="logout()" class="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white font-jua text-xs sm:text-sm border border-slate-700 transition">
            로그아웃
          </button>
        </div>
      </div>
    </header>

    <!-- Student Dashboard Main -->
    <main class="flex-1 max-w-4xl w-full mx-auto p-4 sm:p-6 flex flex-col gap-6">

      <!-- Daily Attendance & Currency Header Bar -->
      <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-3xl flex flex-wrap items-center justify-between gap-3 shadow-md">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-2xl bg-amber-400/20 text-amber-300 flex items-center justify-center text-xl">
            🪙
          </div>
          <div>
            <div class="text-xs text-slate-400 font-medium">보유 해피 포인트</div>
            <div class="text-2xl font-black font-jua text-amber-300 flex items-center gap-1.5">
              <span id="studentViewHappyTop">150</span> <span class="text-sm font-bold text-slate-300">해피</span>
            </div>
          </div>
        </div>

        <!-- Exchange Monster Ball Button (100 Happy = 1 Ball) -->
        <button id="exchangeBallBtn" onclick="exchangeHappyForBall()" class="px-4 py-2.5 rounded-2xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 active:scale-95 text-slate-950 font-jua text-xs sm:text-sm shadow-md transition flex items-center gap-2">
          <span class="mini-ball"></span>
          <span>100 해피로 추가 볼 교환! 🎁</span>
        </button>
      </div>

      <!-- Self Presentation Registration Banner -->
      <div class="bg-gradient-to-r from-emerald-950/60 via-slate-900 to-slate-900 border-2 border-emerald-500/50 rounded-3xl p-5 shadow-xl flex flex-wrap items-center justify-between gap-4">
        <div class="flex items-center gap-3.5">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl flex-shrink-0 border border-emerald-500/30">
            🙋
          </div>
          <div>
            <h3 class="text-lg font-jua text-white mb-0.5">내 생각을 말했나요?</h3>
            <p class="text-xs text-slate-300">선생님이 미처 기록하지 못했다면 직접 발표를 등록하고 볼과 해피를 받으세요!</p>
          </div>
        </div>
        <button onclick="openStudentSelfCheckin()" class="px-4 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 active:scale-95 text-slate-950 font-jua text-sm shadow-md transition flex items-center gap-1.5">
          <span>✨</span> 오늘 발표 셀프 등록
        </button>
      </div>

      <!-- Pending Pokeballs Draw Box -->
      <div class="bg-[#1e293b] border-2 border-rose-500/60 rounded-3xl p-6 sm:p-8 text-center relative overflow-hidden shadow-2xl">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-500/20 border border-rose-400/40 text-rose-300 text-xs font-bold font-jua mb-3">
          <span class="mini-ball"></span>
          <span>수업 중 모은 보상 상자</span>
        </div>

        <div class="my-3 flex items-center justify-center gap-3">
          <span class="text-base sm:text-lg text-slate-300 font-medium">열 수 있는 몬스터볼:</span>
          <span id="studentViewBallCount" class="text-4xl sm:text-5xl font-jua text-rose-400 font-black animate-pulse">0개</span>
        </div>

        <button id="studentViewOpenBallBtn" onclick="studentOpenBall()" class="w-full max-w-md mx-auto mt-3 py-4 rounded-2xl bg-gradient-to-r from-rose-500 via-amber-500 to-orange-500 hover:from-rose-400 hover:to-orange-400 active:scale-95 text-slate-950 font-jua text-lg sm:text-xl shadow-xl transition flex items-center justify-center gap-2.5">
          <span class="w-6 h-6 rounded-full pokeball-btn shadow"></span>
          <span>지금 몬스터볼 열어서 포켓몬 뽑기! 🚀</span>
        </button>
        <p id="studentViewNoBallMsg" class="hidden text-xs text-slate-400 mt-3">열 수 있는 몬스터볼이 없습니다. 발표를 하거나 100 해피를 모아 추가 볼을 교환해보세요!</p>
      </div>

      <!-- Representative Pokemon Card & Training Box -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
        <!-- Rep Pokemon Status -->
        <div class="bg-[#1e293b] border border-slate-700 rounded-3xl p-5 shadow-lg flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold text-amber-300 flex items-center gap-1 font-jua">
                <span>👑</span> 나의 대표 포켓몬
              </span>
              <span id="studentViewTierBadge" class="text-xs px-2.5 py-0.5 rounded-full font-bold bg-amber-700 text-amber-100 hidden">
                레벨 2 · 동색
              </span>
            </div>
            
            <!-- 1. Rep is Set -->
            <div id="studentRepSetBox" class="flex items-center gap-4 my-2">
              <div class="w-24 h-24 rounded-2xl bg-slate-900 border-2 border-amber-400/50 flex items-center justify-center p-2 shadow-inner">
                <img id="studentViewRepImg" src="" class="w-full h-full object-contain filter drop-shadow" />
              </div>
              <div class="flex-1">
                <div class="flex items-center gap-2">
                  <h4 id="studentViewRepName" class="text-2xl font-jua text-white mb-1">포켓몬</h4>
                  <button onclick="openPokedexForCurrentStudentView()" class="text-[11px] text-amber-400 hover:text-amber-300 bg-slate-800 px-2 py-0.5 rounded-lg border border-slate-700 transition" title="대표 포켓몬 변경">변경</button>
                </div>
                <p id="studentViewRepLevel" class="text-xs text-slate-300">레벨 2 • 친밀도 7</p>
                <p class="text-xs text-amber-400 font-bold mt-1">🪙 <span id="studentViewHappy">150</span> 해피 보유</p>
              </div>
            </div>

            <!-- 2. Rep is NOT Set (Empty State) -->
            <div id="studentRepEmptyBox" class="hidden flex flex-col items-center justify-center text-center p-4 bg-slate-900/60 rounded-2xl border border-dashed border-amber-400/30 my-2">
              <div class="text-3xl mb-1">👑</div>
              <h4 class="text-base font-jua text-amber-300 mb-0.5">대표 포켓몬 미지정</h4>
              <p id="studentRepEmptyDesc" class="text-xs text-slate-300 mb-3">수집한 포켓몬 중에서 함께 성장할 대표 포켓몬을 골라보세요!</p>
              <button id="studentRepSelectBtn" onclick="openPokedexForCurrentStudentView()" class="px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-slate-950 font-jua text-xs shadow-md transition flex items-center gap-1.5">
                <span>📖</span>
                <span>도감에서 대표 포켓몬 지정하기</span>
              </button>
            </div>
          </div>

          <button id="studentTrainingActionBtn" onclick="openTrainingForCurrentStudentView()" class="w-full mt-4 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 active:scale-95 text-white font-jua text-sm shadow-md transition flex items-center justify-center gap-2">
            <span>🏋️‍♂️</span>
            <span id="studentTrainingActionBtnText">대표 포켓몬 훈련하기 (-50 해피)</span>
          </button>
        </div>

        <!-- My Pokedex Shortcut -->
        <div class="bg-[#1e293b] border border-slate-700 rounded-3xl p-5 shadow-lg flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold text-emerald-400 flex items-center gap-1 font-jua">
                <span>📖</span> 나만의 포켓몬 도감
              </span>
              <span id="studentViewPokedexStats" class="text-xs font-mono text-slate-400">0 / 152종 수집</span>
            </div>

            <p class="text-xs text-slate-300 leading-relaxed my-2">
              수집한 포켓몬 카드를 터치하여 언제든 대표 포켓몬을 변경할 수 있습니다. 152마리 도감을 완성해보세요!
            </p>

            <div class="w-full bg-slate-900 h-3 rounded-full overflow-hidden border border-slate-700 my-3">
              <div id="studentViewProgressBar" class="h-full bg-gradient-to-r from-amber-500 to-emerald-400 rounded-full" style="width: 0%"></div>
            </div>
          </div>

          <button onclick="openPokedexForCurrentStudentView()" class="w-full mt-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-200 hover:text-white font-jua text-sm border border-slate-600 transition flex items-center justify-center gap-2">
            <span>🔍</span>
            <span>전체 도감 열람하기</span>
          </button>
        </div>
      </div>

    </main>

    <footer class="mt-auto py-4 text-center text-xs text-slate-500 border-t border-slate-800/80">
      <p>우리 반 포켓몬 발표 도감 • 학생 개인 전용 화면</p>
    </footer>
  </div>

  <!-- ==================== COMMON MODALS ==================== -->

  <!-- A. "내 생각을 말했나요?" 학생 셀프 체크인 모달 -->
  <div id="selfCheckinModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md hidden transition-opacity duration-200">
    <div class="bg-white text-slate-900 border-4 border-emerald-400/80 rounded-3xl w-full max-w-md p-6 sm:p-7 shadow-2xl flex flex-col relative animate-card-pop">
      <button onclick="closeSelfCheckinModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-800 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center text-sm font-bold transition">
        ✕
      </button>

      <h3 class="text-2xl sm:text-3xl font-jua text-[#1b4332] text-center tracking-tight mb-2">
        내 생각을 말했나요?
      </h3>
      <p class="text-xs sm:text-sm text-slate-600 text-center leading-relaxed mb-4">
        답하기, 내 생각 말하기, 친구 생각에 보태기,<br>궁금한 점 질문하기 모두 좋아요.
      </p>

      <div class="bg-amber-50 border border-amber-200/80 rounded-2xl p-3 text-xs text-amber-800 text-center font-medium mb-4">
        오늘 발표를 등록하면 몬스터볼 1개와 해피 포인트가 지급됩니다!
      </div>

      <!-- Option 1: 직접 손들어 발표했어요 (+15 해피) -->
      <button onclick="executeStudentSelfCheckin('voluntary')" class="w-full mb-3 p-3.5 rounded-2xl bg-emerald-50 hover:bg-emerald-100/80 border-2 border-emerald-400 text-emerald-950 font-jua flex items-center justify-between text-base sm:text-lg shadow-sm transition active:scale-98">
        <span class="flex items-center gap-2">
          <span>🙋</span>
          <span>직접 손들어 발표했어요</span>
        </span>
        <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-amber-300 text-amber-950">
          +15 해피 & 볼 1개
        </span>
      </button>

      <!-- Option 2: 선생님이 시켜서 발표했어요 (+10 해피) -->
      <button onclick="executeStudentSelfCheckin('called')" class="w-full mb-3 p-3.5 rounded-2xl bg-slate-50 hover:bg-slate-100 border-2 border-slate-300 text-slate-800 font-jua flex items-center justify-between text-base sm:text-lg shadow-sm transition active:scale-98">
        <span class="flex items-center gap-2">
          <span>💬</span>
          <span>선생님이 시켜서 발표했어요</span>
        </span>
        <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-amber-300 text-amber-950">
          +10 해피 & 볼 1개
        </span>
      </button>

      <p class="text-xs text-slate-500 text-center leading-normal mb-3">
        발표 방법은 기록으로 남겨요. 누구나 하루 한 번 같은 경험치와 몬스터볼을 받아요.
      </p>

      <button onclick="closeSelfCheckinModal()" class="w-full p-2.5 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-jua text-sm transition">
        🙂 닫기
      </button>
    </div>
  </div>

  <!-- B. "대표 포켓몬 훈련하기" 모달 -->
  <div id="trainingModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md hidden">
    <div class="bg-white text-slate-900 border-4 border-blue-300 rounded-3xl w-full max-w-sm p-6 shadow-2xl flex flex-col relative animate-card-pop">
      <button onclick="closeTrainingModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-800 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center text-sm font-bold transition">
        ✕
      </button>

      <div class="w-14 h-14 rounded-2xl bg-blue-100 text-blue-600 flex items-center justify-center text-2xl mb-3 shadow-inner">
        🏋️‍♂️
      </div>

      <h3 class="text-xl font-jua text-[#1b263b] mb-1">
        대표 포켓몬 훈련하기
      </h3>

      <div class="flex items-baseline gap-2 my-2">
        <span id="trainingHappyPoints" class="text-4xl font-extrabold text-[#1b263b] font-jua">150</span>
        <span class="text-base font-bold text-slate-600">해피</span>
      </div>

      <p class="text-xs text-slate-600 mb-4">
        선택한 포켓몬 레벨 +1 · 하루 한 번 (50 해피 소모)
      </p>

      <div class="w-full bg-amber-50 border border-amber-200 rounded-2xl p-3 flex items-center gap-3 mb-4">
        <div class="w-14 h-14 bg-white rounded-xl border border-amber-200 flex items-center justify-center p-1">
          <img id="trainingPokeImg" src="" class="w-full h-full object-contain filter drop-shadow" />
        </div>
        <div class="flex-1 min-w-0">
          <h4 id="trainingPokeName" class="text-base font-jua text-slate-900">파이리</h4>
          <p id="trainingPokeLevelBadge" class="text-xs font-bold text-amber-700">레벨 2 · 동색</p>
        </div>
      </div>

      <div class="w-full bg-emerald-50/70 border border-emerald-200 rounded-2xl p-2.5 text-[11px] text-emerald-900 text-center font-medium mb-5">
        레벨 2 동색 · 3 은색 · 4 금색 · 5 챔피언
      </div>

      <button id="trainingActionBtn" onclick="executeTraining()" class="w-full py-3 rounded-2xl bg-[#00897b] hover:bg-[#00796b] active:scale-95 text-white font-jua text-sm sm:text-base shadow-md transition">
        훈련하기 (-50 해피, 레벨 +1)
      </button>

      <div class="mt-4 text-center">
        <p class="text-xs text-slate-400 font-jua">훈련하고, 더 강해지고 🔥</p>
      </div>
    </div>
  </div>

  <!-- C. GACHA / ENCOUNTER MODAL -->
  <div id="gachaModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md hidden transition-opacity duration-300">
    <div id="ballStage" class="flex flex-col items-center justify-center text-center">
      <div class="text-amber-300 text-lg sm:text-xl font-jua mb-4 drop-shadow">
        <span id="gachaStudentName" class="text-white text-2xl">OOO</span> 학생의 포켓몬 뽑기!
      </div>
      <div class="text-sm text-slate-300 mb-8 font-medium animate-pulse">과연 어떤 포켓몬이 등장할까요...?</div>

      <div class="relative cursor-pointer select-none" onclick="triggerOpenBall()">
        <div id="wigglingBall" class="w-36 h-36 sm:w-44 sm:h-44 rounded-full pokeball-btn shadow-2xl animate-ball-bounce cursor-pointer transition-transform">
        </div>
        <div id="ballGlow" class="absolute inset-0 rounded-full bg-amber-400/20 blur-xl scale-125 -z-10 animate-pulse"></div>
      </div>

      <div class="mt-8 text-xs text-slate-400">몬스터볼을 터치하거나 잠시 기다리면 열립니다!</div>
    </div>

    <div id="cardStage" class="hidden w-full max-w-sm flex-col items-center">
      <div class="text-center mb-3">
        <p class="text-amber-300 font-jua text-sm sm:text-base tracking-wide">발표 수업에 포켓몬을 넣어봤습니다</p>
      </div>

      <div id="rewardCardContainer" class="w-full rounded-3xl p-6 sm:p-7 relative transition-all duration-300 animate-card-pop holo-card text-slate-900 border-4 border-amber-300 shadow-2xl flex flex-col items-center">
        <button onclick="closeGachaModal()" class="absolute top-4 right-4 text-slate-700 hover:text-black w-8 h-8 rounded-full bg-black/5 hover:bg-black/10 flex items-center justify-center text-lg font-bold transition">
          ✕
        </button>

        <h3 id="rewardPokemonName" class="text-2xl sm:text-3xl font-jua text-slate-900 text-center tracking-tight mt-1">
          파이리
        </h3>

        <div class="mt-1 mb-3">
          <span id="rewardRarityBadge" class="text-xs font-bold px-3 py-0.5 rounded-full bg-slate-800/10 text-slate-700 tracking-wider">
            일반
          </span>
        </div>

        <div class="relative w-48 h-48 sm:w-56 sm:h-56 my-2 flex items-center justify-center">
          <div id="rewardArtworkGlow" class="absolute inset-0 rounded-full bg-amber-300/40 blur-2xl -z-10"></div>
          <img id="rewardPokemonImage" src="" alt="Pokemon" class="w-full h-full object-contain filter drop-shadow-xl transition-transform hover:scale-105" />
        </div>

        <div class="w-full text-center mt-3 pt-3 border-t border-slate-900/10 flex flex-col gap-1">
          <p id="rewardFirstMetDate" class="text-xs sm:text-sm text-slate-700 font-medium">
            처음 만난 날 · 2026. 9. 27.
          </p>
          <p id="rewardMetCount" class="text-sm sm:text-base font-jua text-amber-900">
            1번 만났어요
          </p>
          <p id="rewardLevelFriendship" class="text-xs font-bold text-emerald-800 mt-1">
            포켓몬 레벨 2 · 친밀도 7
          </p>
        </div>

        <!-- Representative Pokemon Setting Button in Gacha Reward -->
        <button id="rewardSetRepBtn" onclick="setRepFromReward()" class="w-full mt-4 py-2.5 rounded-2xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-slate-950 font-jua text-sm shadow-md transition active:scale-95 flex items-center justify-center gap-1.5 cursor-pointer">
          <span>👑</span>
          <span id="rewardSetRepText">이 포켓몬을 대표 포켓몬으로 설정하기</span>
        </button>

        <button onclick="goToPokedexFromGacha()" class="w-full mt-2 py-2.5 rounded-2xl bg-[#00897b] hover:bg-[#00796b] text-white font-jua text-sm sm:text-base shadow-lg transition active:scale-95">
          도감으로
        </button>
      </div>

      <div class="mt-3 text-center">
        <span class="text-xs text-slate-300 bg-slate-800/80 px-3 py-1 rounded-full border border-slate-700">
          수집 학생: <span id="rewardStudentBadge" class="text-amber-300 font-bold">강해나</span>
        </span>
      </div>
    </div>
  </div>

  <!-- D. STUDENT POKEDEX MODAL -->
  <div id="pokedexModal" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/85 backdrop-blur-md hidden">
    <div class="bg-[#1e293b] border border-slate-700 rounded-3xl w-full max-w-5xl max-h-[92vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="p-4 sm:p-5 border-b border-slate-700/80 flex items-center justify-between bg-slate-800/50">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-2xl bg-amber-400/20 text-amber-300 flex items-center justify-center text-xl font-jua border border-amber-400/30">
            📖
          </div>
          <div>
            <h3 class="text-lg sm:text-xl font-jua text-white flex items-center gap-2">
              <span id="pokedexStudentName" class="text-amber-300">강해나</span> 학생의 포켓몬 도감
            </h3>
            <p id="pokedexStudentStats" class="text-xs text-slate-400">발표 0회 • 수집 0 / 152종 (0%) • 150 해피</p>
          </div>
        </div>
        <button onclick="closePokedexModal()" class="w-8 h-8 rounded-full bg-slate-700 hover:bg-slate-600 text-slate-300 flex items-center justify-center transition">
          ✕
        </button>
      </div>

      <div class="px-5 py-2.5 bg-slate-900 border-b border-slate-800 flex items-center justify-between">
        <span class="text-amber-300 font-jua text-xs sm:text-sm tracking-wide">
          🌟 나만의 도감을 채우는 재미 (수집한 카드를 터치하면 대표 포켓몬으로 설정됩니다)
        </span>
      </div>

      <div class="px-5 py-3 bg-slate-900/60 border-b border-slate-700/50 flex flex-wrap items-center justify-between gap-3 text-xs">
        <div class="flex-1 min-w-[200px]">
          <div class="flex justify-between mb-1 font-medium">
            <span class="text-slate-400">도감 완성도</span>
            <span id="pokedexPercentText" class="text-amber-400 font-bold">0%</span>
          </div>
          <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden border border-slate-700">
            <div id="pokedexProgressBar" class="h-full bg-gradient-to-r from-amber-500 to-emerald-400 rounded-full transition-all duration-500" style="width: 0%"></div>
          </div>
        </div>

        <div class="flex items-center gap-1 bg-slate-800 p-1 rounded-xl border border-slate-700">
          <button onclick="filterPokedex('all')" id="filterTabAll" class="px-2.5 py-1 rounded-lg bg-amber-500 text-slate-900 font-bold transition">전체 (152)</button>
          <button onclick="filterPokedex('collected')" id="filterTabCollected" class="px-2.5 py-1 rounded-lg text-slate-300 hover:text-white transition">수집 완료</button>
          <button onclick="filterPokedex('uncollected')" id="filterTabUncollected" class="px-2.5 py-1 rounded-lg text-slate-300 hover:text-white transition">미수집</button>
        </div>
      </div>

      <div class="flex-1 overflow-y-auto p-4 sm:p-5 bg-slate-900/40">
        <div id="pokedexGrid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 gap-3 sm:gap-4">
        </div>
      </div>

      <div class="p-3 bg-slate-800/50 border-t border-slate-700/80 text-center text-xs text-slate-400">
        수집한 포켓몬 카드를 클릭하면 👑 대표 포켓몬으로 지정할 수 있습니다.
      </div>
    </div>
  </div>

  <!-- E. RANDOM ROULETTE MODAL -->
  <div id="rouletteModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md hidden">
    <div class="bg-[#1e293b] border border-slate-700 rounded-3xl w-full max-w-md p-6 shadow-2xl flex flex-col items-center text-center">
      <div class="w-12 h-12 rounded-2xl bg-orange-500/20 text-orange-400 flex items-center justify-center text-2xl font-jua mb-3 border border-orange-500/30">
        🎲
      </div>
      <h3 class="text-xl font-jua text-white mb-1">랜덤 발표자 추첨</h3>
      <p class="text-xs text-slate-400 mb-6">누가 멋지게 발표해 볼까요?</p>

      <div class="w-full bg-slate-900 border-2 border-amber-500/40 rounded-2xl p-6 mb-6 shadow-inner relative overflow-hidden flex flex-col items-center justify-center min-h-[140px]">
        <div id="rouletteNumberBadge" class="text-xs font-bold text-amber-400 bg-amber-400/10 border border-amber-400/20 px-2.5 py-0.5 rounded-full mb-2">
          번호 대기중
        </div>
        <div id="rouletteNameDisplay" class="text-3xl sm:text-4xl font-jua text-white tracking-wider">
          준비 완료!
        </div>
      </div>

      <div id="rouletteInitialBtns" class="flex items-center gap-3 w-full">
        <button onclick="startRouletteSpin()" class="flex-1 py-3 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 active:scale-95 text-slate-900 font-jua text-base shadow-lg transition">
          추첨 시작! 🚀
        </button>
        <button onclick="closeRouletteModal()" class="px-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-sm transition">
          닫기
        </button>
      </div>

      <div id="rouletteWinnerBtns" class="hidden flex-col gap-2.5 w-full">
        <button onclick="saveWinnerBallOnly()" class="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-jua text-sm sm:text-base shadow-lg transition active:scale-95 flex items-center justify-center gap-2">
          <span class="mini-ball"></span>
          <span>수업 후 뽑기로 몬스터볼 적립 (+1)</span>
        </button>
        <button onclick="openWinnerGachaNow()" class="w-full py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-jua text-sm shadow transition active:scale-95">
          지금 바로 포켓몬 뽑기! ✨
        </button>
      </div>
    </div>
  </div>

  <!-- F. MANAGE / SETTINGS MODAL -->
  <div id="manageModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md hidden">
    <div class="bg-[#1e293b] border border-slate-700 rounded-3xl w-full max-w-3xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="p-5 border-b border-slate-700 flex items-center justify-between bg-slate-800/50">
        <div class="flex items-center gap-3">
          <span class="text-2xl">⚙️</span>
          <div>
            <h3 class="text-lg font-jua text-white">학급 명단, 비밀번호 및 포인트 규칙 관리</h3>
            <p class="text-xs text-slate-400">포인트 획득 규칙과 볼 교환 비용을 설정합니다.</p>
          </div>
        </div>
        <button onclick="closeManageModal()" class="w-8 h-8 rounded-full bg-slate-700 hover:bg-slate-600 text-slate-300 flex items-center justify-center transition">
          ✕
        </button>
      </div>

      <div class="p-5 flex-1 overflow-y-auto space-y-6 text-sm">
        <!-- Economy Settings Box -->
        <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-700/80">
          <h4 class="font-jua text-amber-300 mb-2 flex items-center gap-1.5">
            <span>🪙</span> 해피 포인트 & 볼 교환 규칙 설정
          </h4>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
            <div class="bg-slate-800 p-3 rounded-xl border border-slate-700">
              <label class="block text-slate-400 mb-1">매일 출석 기본 포인트</label>
              <div class="flex items-center gap-2">
                <input type="number" id="settingDailyHappy" value="20" min="0" step="5" class="w-20 p-1.5 bg-slate-900 border border-slate-600 rounded text-center text-amber-300 font-bold" />
                <span>해피</span>
              </div>
            </div>
            <div class="bg-slate-800 p-3 rounded-xl border border-slate-700">
              <label class="block text-slate-400 mb-1">발표 1회당 적립 포인트</label>
              <div class="flex items-center gap-2">
                <input type="number" id="settingPresentHappy" value="15" min="0" step="5" class="w-20 p-1.5 bg-slate-900 border border-slate-600 rounded text-center text-amber-300 font-bold" />
                <span>해피</span>
              </div>
            </div>
            <div class="bg-slate-800 p-3 rounded-xl border border-slate-700">
              <label class="block text-slate-400 mb-1">몬스터볼 1개 교환 비용</label>
              <div class="flex items-center gap-2">
                <input type="number" id="settingBallCost" value="100" min="10" step="10" class="w-20 p-1.5 bg-slate-900 border border-slate-600 rounded text-center text-rose-300 font-bold" />
                <span>해피</span>
              </div>
            </div>
          </div>
          <div class="mt-3 flex justify-end">
            <button onclick="saveEconomySettings()" class="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-jua text-xs transition">
              규칙 저장
            </button>
          </div>
        </div>

        <!-- Teacher Password Setting -->
        <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-700/80 flex flex-wrap items-center justify-between gap-3">
          <div>
            <h4 class="font-jua text-amber-300">선생님 로그인 비밀번호</h4>
            <p class="text-xs text-slate-400">현재 선생님 비밀번호를 변경할 수 있습니다.</p>
          </div>
          <button onclick="changeTeacherPasswordPrompt()" class="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 text-xs font-jua transition">
            비밀번호 변경
          </button>
        </div>

        <!-- Cloud Sync (Firebase) Setting -->
        <div class="bg-slate-900/80 p-4 sm:p-5 rounded-2xl border border-slate-700/80">
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center gap-2">
              <span class="text-xl">☁️</span>
              <h4 class="font-jua text-white text-base">실시간 클라우드 서버 연동 (Firebase 무료)</h4>
            </div>
            <span id="cloudModalStatusSmall" class="text-xs px-2.5 py-0.5 rounded-full font-jua bg-slate-800 text-slate-400 border border-slate-700">미연동</span>
          </div>
          
          <p id="cloudModalStatusText" class="text-xs text-slate-300 leading-relaxed mb-3">
            선생님 PC와 학생들의 폰/태블릿 간에 실시간으로 발표 기록과 포켓몬 데이터를 공유하려면 구글 파이어베이스(100% 무료)를 연동하세요.
          </p>

          <div class="space-y-3">
            <div>
              <label class="block text-[11px] text-slate-400 font-medium mb-1">학급 고유 식별 코드 (영문/숫자)</label>
              <input id="settingClassId" type="text" placeholder="예: happy-class-5-1" value="classroom_5_default" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-amber-400 font-mono" />
            </div>

            <div>
              <label class="block text-[11px] text-slate-400 font-medium mb-1">
                Firebase 설정 코드 붙여넣기 (콘솔에서 복사한 firebaseConfig)
              </label>
              <textarea id="settingFirebaseConfig" rows="3" placeholder='예: const firebaseConfig = { apiKey: "...", projectId: "...", ... };' class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-xs text-amber-200 focus:outline-none focus:border-amber-400 font-mono"></textarea>
            </div>

            <div class="flex items-center gap-2 flex-wrap pt-1">
              <button onclick="saveCloudConfigFromModal()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-jua text-xs shadow-md transition active:scale-95 flex items-center gap-1.5 cursor-pointer">
                <span>☁️</span>
                <span>클라우드 서버 연동 및 동기화 시작</span>
              </button>
              <button onclick="pushLocalDataToCloudManual()" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 text-xs font-jua transition cursor-pointer">
                <span>⬆️ 로컬 데이터 서버로 업로드</span>
              </button>
              <button onclick="disconnectCloudSync()" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-rose-900/40 text-rose-300 border border-slate-700 text-xs font-jua transition cursor-pointer">
                연동 해제
              </button>
              <button onclick="toggleFirebaseHelp()" class="text-xs text-amber-300 underline ml-auto font-jua cursor-pointer">
                📖 3분 무료 Firebase 생성 방법
              </button>
            </div>

            <!-- Firebase Step-by-Step Guide Accordion -->
            <div id="firebaseHelpBox" class="hidden mt-3 p-3.5 bg-slate-950/70 border border-amber-400/30 rounded-xl text-xs text-slate-300 space-y-2">
              <h5 class="font-jua text-amber-300 text-sm">💡 초간단 3분 Firebase 연동 순서 (100% 평생 무료)</h5>
              <ol class="list-decimal list-inside space-y-1.5 text-[11px] text-slate-300">
                <li><a href="https://console.firebase.google.com" target="_blank" class="text-emerald-400 underline font-bold">Google Firebase 콘솔 (링크)</a>에 구글 계정으로 로그인합니다.</li>
                <li><strong>[프로젝트 만들기]</strong>를 클릭하고 프로젝트 이름(예: <code class="bg-slate-800 px-1 rounded text-amber-300">pocketmon-class</code>)을 입력하여 생성합니다.</li>
                <li>좌측 메뉴 <strong>[빌드] → [Firestore Database]</strong> 클릭 → <strong>[데이터베이스 만들기]</strong> → 위치 선택 후 <strong>[테스트 모드에서 시작]</strong> 선택 후 [사용 설정] 클릭합니다.</li>
                <li>프로젝트 개요 옆의 <strong>톱니바퀴 ⚙️ (프로젝트 설정)</strong> 클릭 → 하단 [내 앱]에서 <strong>웹(&lt;/&gt;)</strong> 아이콘 클릭하여 앱 등록!</li>
                <li>화면에 나오는 <code class="bg-slate-800 px-1 rounded text-amber-300">const firebaseConfig = { ... }</code> 코드 블록을 복사하여 위 입력창에 그대로 붙여넣고 [클라우드 서버 연동]을 누르면 끝!</li>
              </ol>
            </div>
          </div>
        </div>

        <!-- Backup & Restore -->
        <div class="bg-slate-900/70 p-4 rounded-2xl border border-slate-700/60">
          <h4 class="font-jua text-amber-300 mb-2 flex items-center gap-1.5">
            <span>💾</span> 데이터 백업 및 복원
          </h4>
          <p class="text-xs text-slate-400 mb-4">현재 모든 학생의 발표 기록, 레벨, 비밀번호, 도감 데이터를 파일로 저장하거나 불러옵니다.</p>
          <div class="flex flex-wrap gap-2.5">
            <button onclick="exportData()" class="px-3.5 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-medium text-xs flex items-center gap-1.5 transition">
              <span>📥</span> JSON 파일로 백업 다운로드
            </button>
            <label class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600 font-medium text-xs flex items-center gap-1.5 cursor-pointer transition">
              <span>📤</span> 백업 파일 불러오기
              <input type="file" id="importFileInput" accept=".json" class="hidden" onchange="importData(event)">
            </label>
            <button onclick="resetAllDataConfirm()" class="px-3.5 py-2 rounded-xl bg-red-900/40 hover:bg-red-800/60 border border-red-700 text-red-200 font-medium text-xs flex items-center gap-1.5 transition ml-auto">
              <span>⚠️</span> 발표 데이터 초기화
            </button>
          </div>
        </div>

        <!-- Student List with Passwords & Points -->
        <div>
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-jua text-slate-200 flex items-center gap-1.5">
              <span>📋</span> 학생 명단 및 포인트 현황 (<span id="manageStudentCount">16</span>명)
            </h4>
            <button onclick="addNewStudentPrompt()" class="px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition flex items-center gap-1">
              <span>+</span> 학생 추가
            </button>
          </div>

          <div class="max-h-72 overflow-y-auto border border-slate-700 rounded-xl bg-slate-900/50 divide-y divide-slate-800" id="manageStudentList">
          </div>
        </div>
      </div>

      <div class="p-4 bg-slate-800/50 border-t border-slate-700 flex justify-end">
        <button onclick="closeManageModal()" class="px-5 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-white font-medium text-xs transition">
          닫기
        </button>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT APPLICATION LOGIC -->
  <script>
    const POKEMON_DATA = __POKEMON_DATA_JSON__;

    /* Sound Synthesizer */
    class RetroSoundManager {
      constructor() {
        this.ctx = null;
        this.enabled = true;
      }
      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
        }
        if (this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }
      playTick() {
        if (!this.enabled) return;
        this.init();
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(440, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(120, this.ctx.currentTime + 0.05);
        gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.05);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.05);
      }
      playOpenBall() {
        if (!this.enabled) return;
        this.init();
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(300, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(1200, this.ctx.currentTime + 0.25);
        gain.gain.setValueAtTime(0.3, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.25);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.25);
      }
      playFanfare(isLegendary = false) {
        if (!this.enabled) return;
        this.init();
        const now = this.ctx.currentTime;
        const notes = isLegendary 
          ? [523.25, 659.25, 783.99, 987.77, 1046.50, 1318.51] 
          : [523.25, 659.25, 783.99, 1046.50];
        
        notes.forEach((freq, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = isLegendary ? 'sawtooth' : 'triangle';
          osc.frequency.setValueAtTime(freq, now + idx * 0.1);
          gain.gain.setValueAtTime(0.25, now + idx * 0.1);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.1 + 0.35);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.1);
          osc.stop(now + idx * 0.1 + 0.35);
        });
      }
      playWinJingle() {
        if (!this.enabled) return;
        this.init();
        const now = this.ctx.currentTime;
        [587.33, 739.99, 880.00].forEach((freq, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(freq, now + i * 0.08);
          gain.gain.setValueAtTime(0.15, now + i * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.2);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.08);
          osc.stop(now + i * 0.08 + 0.2);
        });
      }
      playLevelUp() {
        if (!this.enabled) return;
        this.init();
        const now = this.ctx.currentTime;
        [440, 554.37, 659.25, 880].forEach((freq, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + i * 0.07);
          gain.gain.setValueAtTime(0.2, now + i * 0.07);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.07 + 0.2);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.07);
          osc.stop(now + i * 0.07 + 0.2);
        });
      }
      playBallAward() {
        if (!this.enabled) return;
        this.init();
        const now = this.ctx.currentTime;
        [523.25, 659.25].forEach((freq, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + i * 0.09);
          gain.gain.setValueAtTime(0.2, now + i * 0.09);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.09 + 0.15);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.09);
          osc.stop(now + i * 0.09 + 0.15);
        });
      }
    }
    const soundManager = new RetroSoundManager();

    /* State Management */
    const STORAGE_KEY = 'pocketmon_classroom_data_v5';
    let appState = {
      className: '행복한 5학년의 발표 포켓몬',
      teacherPassword: '1234',
      // Happy point rules
      dailyHappyBonus: 20,     // 매일 출석 시 기본 지급 포인트
      presentHappyBonus: 15,   // 발표 1회당 추가 지급 포인트
      ballExchangeCost: 100,   // 추가 몬스터볼 교환 필요 포인트
      students: __INITIAL_STUDENTS_JSON__,
      soundEnabled: true,
      lastDate: new Date().toISOString().split('T')[0],
      currentSession: null,
      // Cloud sync config (Firebase)
      classId: 'classroom_pocketmon_main',
      firebaseConfig: {
        apiKey: "AIzaSyCTkOPaxO2p-S92jvrtn7lzaddAkUF9ecQ",
        authDomain: "ocketmon-classroom.firebaseapp.com",
        projectId: "ocketmon-classroom",
        storageBucket: "ocketmon-classroom.firebasestorage.app",
        messagingSenderId: "149388375699",
        appId: "1:149388375699:web:b0af98c418e4e77f137f66",
        measurementId: "G-BJYF4H4T7T"
      },
    };

    /* Cloud Sync Engine (Firebase Realtime Firestore) */
    let firestoreDb = null;
    let unsubscribeFirestore = null;
    let isRemoteUpdate = false;
    let isCloudSaving = false;

    function initCloudSync() {
      const config = appState.firebaseConfig || (window.FIREBASE_CONFIG && window.FIREBASE_CONFIG.apiKey ? window.FIREBASE_CONFIG : null);
      if (!window.firebase || !config) {
        updateCloudStatusUI(false);
        return;
      }
      appState.firebaseConfig = config;

      try {
        if (!firebase.apps || firebase.apps.length === 0) {
          firebase.initializeApp(config);
        }
        firestoreDb = firebase.firestore();
        const docId = (appState.classId || 'classroom_5_default').trim();
        const docRef = firestoreDb.collection('classrooms').doc(docId);

        if (unsubscribeFirestore) {
          unsubscribeFirestore();
        }

        unsubscribeFirestore = docRef.onSnapshot((docSnapshot) => {
          if (docSnapshot.exists) {
            const data = docSnapshot.data();
            if (data && !isCloudSaving) {
              isRemoteUpdate = true;
              applyCloudState(data);
              isRemoteUpdate = false;
            }
          } else {
            // First time: upload local data to cloud
            pushStateToCloud();
          }
          updateCloudStatusUI(true);
        }, (err) => {
          console.error('Firebase sync listener error:', err);
          updateCloudStatusUI(false, err.message);
        });
      } catch (err) {
        console.error('Firebase init error:', err);
        updateCloudStatusUI(false, err.message);
      }
    }

    function pushStateToCloud() {
      if (!firestoreDb || !appState.firebaseConfig) return;
      const docId = (appState.classId || 'classroom_5_default').trim();
      const docRef = firestoreDb.collection('classrooms').doc(docId);

      isCloudSaving = true;
      const payload = {
        className: appState.className,
        teacherPassword: appState.teacherPassword,
        dailyHappyBonus: appState.dailyHappyBonus || 20,
        presentHappyBonus: appState.presentHappyBonus || 15,
        ballExchangeCost: appState.ballExchangeCost || 100,
        students: appState.students,
        lastDate: appState.lastDate,
        updatedAt: Date.now()
      };

      docRef.set(payload, { merge: true })
        .then(() => {
          isCloudSaving = false;
          updateCloudStatusUI(true);
        })
        .catch((err) => {
          isCloudSaving = false;
          console.error('Cloud save failed:', err);
          updateCloudStatusUI(false, err.message);
        });
    }

    function applyCloudState(data) {
      if (!data) return;
      if (data.className) appState.className = data.className;
      if (data.teacherPassword) appState.teacherPassword = data.teacherPassword;
      if (data.dailyHappyBonus !== undefined) appState.dailyHappyBonus = data.dailyHappyBonus;
      if (data.presentHappyBonus !== undefined) appState.presentHappyBonus = data.presentHappyBonus;
      if (data.ballExchangeCost !== undefined) appState.ballExchangeCost = data.ballExchangeCost;
      if (data.lastDate) appState.lastDate = data.lastDate;
      if (Array.isArray(data.students)) {
        appState.students = data.students;
      }

      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
      } catch (e) {}

      updateGlobalStats();
      if (appState.currentSession) {
        if (appState.currentSession.role === 'teacher') {
          renderStudentGrid();
          renderManageStudentList();
        } else if (appState.currentSession.role === 'student') {
          renderStudentView(appState.currentSession.studentId);
        }
      }
      populateLoginStudentDropdown();
    }

    function updateCloudStatusUI(isConnected, errorMsg) {
      const badges = document.querySelectorAll('.cloud-sync-badge');
      badges.forEach(badge => {
        if (isConnected) {
          badge.className = "cloud-sync-badge flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-jua";
          badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span><span>☁️ 서버 실시간 연동 중</span>`;
          badge.title = "구글 파이어베이스 클라우드 서버와 실시간 동기화 중입니다.";
        } else {
          badge.className = "cloud-sync-badge flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-800 border border-slate-700 text-slate-400 hover:text-amber-300 text-xs font-jua cursor-pointer transition";
          badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-slate-500"></span><span>💾 로컬 모드 (${errorMsg ? '연결 오류' : '서버 미연동'})</span>`;
          badge.title = errorMsg ? `연동 오류: ${errorMsg}` : "현재 기기에만 저장되는 로컬 모드입니다. 클릭하여 서버를 연동하세요.";
          badge.onclick = () => {
            if (appState.currentSession && appState.currentSession.role === 'teacher') {
              openManageModal();
            } else {
              alert('선생님 모드로 로그인하시면 100% 무료 클라우드 서버(Firebase)를 연동할 수 있습니다.');
            }
          };
        }
      });

      const modalStatus = document.getElementById('cloudModalStatusText');
      const smallStatus = document.getElementById('cloudModalStatusSmall');
      if (modalStatus) {
        if (isConnected) {
          modalStatus.innerHTML = `<span class="text-emerald-400 font-bold">🟢 정상 연결됨</span> - 모든 기기(선생님 PC, 학생 태블릿/폰)에서 실시간으로 데이터가 저장·공유되고 있습니다.`;
          if (smallStatus) {
            smallStatus.className = "text-xs px-2.5 py-0.5 rounded-full font-jua bg-emerald-500/20 text-emerald-300 border border-emerald-500/40";
            smallStatus.textContent = "🟢 실시간 연결됨";
          }
        } else {
          modalStatus.innerHTML = `<span class="text-slate-400 font-bold">⚪ 미연동 (로컬 모드)</span> - 현재는 각 기기의 브라우저에만 저장됩니다. 아래 설정을 완료하면 모든 기기가 실시간으로 연결됩니다.`;
          if (smallStatus) {
            smallStatus.className = "text-xs px-2.5 py-0.5 rounded-full font-jua bg-slate-800 text-slate-400 border border-slate-700";
            smallStatus.textContent = "미연동";
          }
        }
      }
    }

    function parseFirebaseConfigInput(raw) {
      if (!raw || !raw.trim()) return null;
      let text = raw.trim();
      try {
        return JSON.parse(text);
      } catch (e) {}
      const match = text.match(/\{[\s\S]*\}/);
      if (match) {
        try {
          const fn = new Function('return (' + match[0] + ');');
          const obj = fn();
          if (obj && typeof obj === 'object') return obj;
        } catch (e) {}
      }
      return null;
    }

    function saveCloudConfigFromModal() {
      const classIdInput = document.getElementById('settingClassId').value.trim() || 'classroom_5_default';
      const rawConfig = document.getElementById('settingFirebaseConfig').value;
      const parsed = parseFirebaseConfigInput(rawConfig);

      if (!parsed || !parsed.apiKey || !parsed.projectId) {
        alert('올바른 Firebase 설정(apiKey, projectId 포함)을 입력해주세요.\\n(Firebase 콘솔에서 복사한 const firebaseConfig = { ... } 코드를 그대로 붙여넣으시면 됩니다)');
        return;
      }

      appState.classId = classIdInput;
      appState.firebaseConfig = parsed;
      saveState();
      initCloudSync();
      pushStateToCloud();
      alert('☁️ 클라우드 서버 설정이 저장되었습니다!\\n현재 학급 데이터가 서버로 업로드되어 실시간 동기화가 시작됩니다. 🎉');
    }

    function disconnectCloudSync() {
      if (!confirm('정말로 클라우드 서버 연동을 해제하고 로컬 모드로 전환하시겠습니까?\\n(기존 로컬 데이터는 유지됩니다)')) return;
      if (unsubscribeFirestore) {
        unsubscribeFirestore();
        unsubscribeFirestore = null;
      }
      firestoreDb = null;
      appState.firebaseConfig = null;
      saveState();
      updateCloudStatusUI(false);
      updateSettingsInputs();
      alert('클라우드 연동이 해제되어 로컬 모드로 전환되었습니다.');
    }

    function pushLocalDataToCloudManual() {
      if (!firestoreDb || !appState.firebaseConfig) {
        alert('먼저 Firebase 설정을 입력하고 연동을 시작해주세요.');
        return;
      }
      pushStateToCloud();
      alert('현재 로컬 학급 데이터가 클라우드 서버로 성공적으로 전송되었습니다! 🚀');
    }

    function toggleFirebaseHelp() {
      const box = document.getElementById('firebaseHelpBox');
      if (box) box.classList.toggle('hidden');
    }

    function loadState() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
          const parsed = JSON.parse(saved);
          if (parsed && Array.isArray(parsed.students)) {
            appState = { ...appState, ...parsed };
          }
        }
      } catch (e) {
        console.error('Failed to load state from localStorage:', e);
      }

      // Sanitize representativePokeId: must be null or present in collected map
      if (appState.students) {
        appState.students.forEach(s => {
          if (!s.collected) s.collected = {};
          if (s.representativePokeId && !s.collected[s.representativePokeId]) {
            s.representativePokeId = null;
          }
        });
      }

      // Check daily date rollover & award daily happy points
      const today = new Date().toISOString().split('T')[0];
      if (appState.lastDate !== today) {
        appState.lastDate = today;
        appState.students.forEach(s => {
          s.todayLog = null;
          s.trainedToday = false;
        });
        saveState();
      }

      // Initialize Cloud Sync if config exists
      if ((!appState.firebaseConfig || !appState.firebaseConfig.apiKey) && window.FIREBASE_CONFIG && window.FIREBASE_CONFIG.apiKey) {
        appState.firebaseConfig = window.FIREBASE_CONFIG;
      }
      if (!appState.classId || appState.classId === 'classroom_5_default') {
        appState.classId = 'classroom_pocketmon_main';
      }
      if (appState.firebaseConfig) {
        initCloudSync();
      } else {
        updateCloudStatusUI(false);
      }

      soundManager.enabled = appState.soundEnabled !== false;
      updateSoundUI();
      populateLoginStudentDropdown();
      updateSettingsInputs();

      if (appState.currentSession) {
        applySession(appState.currentSession);
      } else {
        showLoginScreen();
      }
    }

    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
      } catch (e) {
        console.error('Failed to save state to localStorage:', e);
      }
      updateGlobalStats();

      // If connected to cloud, push to cloud as well
      if (firestoreDb && appState.firebaseConfig && !isRemoteUpdate) {
        pushStateToCloud();
      }
    }

    function toggleSound() {
      appState.soundEnabled = !appState.soundEnabled;
      soundManager.enabled = appState.soundEnabled;
      updateSoundUI();
      saveState();
      if (soundManager.enabled) {
        soundManager.playTick();
      }
    }
    function updateSoundUI() {
      const btn = document.getElementById('soundToggleBtn');
      if (btn) {
        btn.textContent = soundManager.enabled ? '🔊' : '🔇';
        btn.classList.toggle('text-slate-500', !soundManager.enabled);
      }
    }

    function showToast(message) {
      const toast = document.getElementById('toastAlert');
      const msgSpan = document.getElementById('toastMessage');
      if (!toast || !msgSpan) return;
      msgSpan.textContent = message;
      toast.classList.remove('opacity-0', 'pointer-events-none', '-translate-y-4');
      toast.classList.add('opacity-100', 'translate-y-0');
      setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'pointer-events-none', '-translate-y-4');
      }, 2400);
    }

    function getLevelTier(lvl) {
      if (lvl >= 5) return { name: '챔피언', badgeClass: 'bg-gradient-to-r from-amber-400 to-red-500 text-white font-bold', border: 'border-red-500' };
      if (lvl === 4) return { name: '금색', badgeClass: 'bg-amber-400 text-slate-950 font-bold', border: 'border-amber-400' };
      if (lvl === 3) return { name: '은색', badgeClass: 'bg-slate-300 text-slate-900 font-bold', border: 'border-slate-300' };
      if (lvl === 2) return { name: '동색', badgeClass: 'bg-amber-700 text-amber-100 font-bold', border: 'border-amber-700' };
      return { name: '기본', badgeClass: 'bg-slate-700 text-slate-300 font-medium', border: 'border-slate-600' };
    }

    /* Check & award Daily Attendance Happy Points when student logs in */
    function checkDailyAttendance(student) {
      const today = new Date().toISOString().split('T')[0];
      if (student.lastAttendance !== today) {
        student.lastAttendance = today;
        const dailyBonus = appState.dailyHappyBonus || 20;
        student.happy = (student.happy || 0) + dailyBonus;
        saveState();
        showToast(`🎉 오늘의 출석 보너스! +${dailyBonus} 해피가 지급되었습니다!`);
        soundManager.playLevelUp();
      }
    }

    /* ==================== AUTHENTICATION ==================== */
    function populateLoginStudentDropdown() {
      const sel = document.getElementById('loginStudentSelect');
      if (!sel) return;
      sel.innerHTML = '';
      appState.students.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s.id;
        opt.textContent = `${s.number}번 ${s.name}`;
        sel.appendChild(opt);
      });
    }

    function switchLoginTab(role) {
      soundManager.playTick();
      const tabStudent = document.getElementById('tabStudentBtn');
      const tabTeacher = document.getElementById('tabTeacherBtn');
      const studentForm = document.getElementById('studentLoginForm');
      const teacherForm = document.getElementById('teacherLoginForm');

      if (role === 'student') {
        tabStudent.className = "py-2.5 rounded-xl font-jua text-sm transition bg-emerald-500 text-slate-950 font-bold shadow";
        tabTeacher.className = "py-2.5 rounded-xl font-jua text-sm transition text-slate-300 hover:text-white";
        studentForm.classList.remove('hidden');
        teacherForm.classList.add('hidden');
      } else {
        tabTeacher.className = "py-2.5 rounded-xl font-jua text-sm transition bg-amber-500 text-slate-950 font-bold shadow";
        tabStudent.className = "py-2.5 rounded-xl font-jua text-sm transition text-slate-300 hover:text-white";
        teacherForm.classList.remove('hidden');
        studentForm.classList.add('hidden');
      }
    }

    function handleStudentLogin(e) {
      e.preventDefault();
      soundManager.init();
      const select = document.getElementById('loginStudentSelect');
      const pwInput = document.getElementById('loginStudentPw');
      const studentId = parseInt(select.value);
      const student = appState.students.find(s => s.id === studentId);

      if (!student) {
        alert('학생 정보를 찾을 수 없습니다.');
        return;
      }

      const inputPw = pwInput.value.trim();
      const actualPw = student.password || String(student.number).padStart(4, '0');

      if (inputPw !== actualPw) {
        alert('비밀번호가 올바르지 않습니다. (선생님께 확인해보세요!)');
        pwInput.value = '';
        pwInput.focus();
        return;
      }

      pwInput.value = '';
      appState.currentSession = { role: 'student', studentId: student.id };
      saveState();

      // Award daily attendance bonus
      checkDailyAttendance(student);

      soundManager.playWinJingle();
      applySession(appState.currentSession);
    }

    function handleTeacherLogin(e) {
      e.preventDefault();
      soundManager.init();
      const pwInput = document.getElementById('loginTeacherPw');
      const inputPw = pwInput.value.trim();
      const actualPw = appState.teacherPassword || '1234';

      if (inputPw !== actualPw) {
        alert('선생님 비밀번호가 올바르지 않습니다.');
        pwInput.value = '';
        pwInput.focus();
        return;
      }

      pwInput.value = '';
      appState.currentSession = { role: 'teacher' };
      saveState();
      soundManager.playFanfare();
      applySession(appState.currentSession);
    }

    function applySession(session) {
      const loginScreen = document.getElementById('loginScreen');
      const teacherView = document.getElementById('teacherView');
      const studentView = document.getElementById('studentView');

      if (!session) {
        showLoginScreen();
        return;
      }

      loginScreen.classList.add('hidden');

      if (session.role === 'teacher') {
        teacherView.classList.remove('hidden');
        studentView.classList.add('hidden');
        renderStudentGrid();
      } else if (session.role === 'student') {
        teacherView.classList.add('hidden');
        studentView.classList.remove('hidden');
        renderStudentView(session.studentId);
      }
    }

    function showLoginScreen() {
      document.getElementById('loginScreen').classList.remove('hidden');
      document.getElementById('teacherView').classList.add('hidden');
      document.getElementById('studentView').classList.add('hidden');
      populateLoginStudentDropdown();
    }

    function logout() {
      appState.currentSession = null;
      saveState();
      soundManager.playTick();
      showLoginScreen();
    }

    /* ==================== TEACHER VIEW ==================== */
    function renderStudentGrid() {
      const grid = document.getElementById('studentGrid');
      grid.innerHTML = '';

      document.getElementById('studentTotalCount').textContent = appState.students.length;
      document.getElementById('headerClassName').textContent = appState.className || '우리 반 발표 포켓몬';

      appState.students.forEach(student => {
        const collectedMap = student.collected || {};
        const collectedCount = Object.keys(collectedMap).length;
        const pendingBalls = student.pendingBalls || 0;
        
        const repId = student.representativePokeId;
        const repPoke = (repId && collectedMap[repId]) ? POKEMON_DATA.find(p => p.id === repId) : null;
        const repData = repPoke ? collectedMap[repId] : null;
        const tier = repData ? getLevelTier(repData.level || 1) : null;

        const card = document.createElement('div');
        card.className = "group relative bg-[#1e293b] hover:bg-[#273549] border-2 border-slate-700/80 hover:border-emerald-400/80 rounded-2xl p-4 transition-all duration-200 shadow-md hover:shadow-xl flex flex-col justify-between select-none cursor-pointer";
        
        card.onclick = () => openPokedexForStudent(student.id);

        let todayBadgeHtml = '';
        if (student.todayLog === 'voluntary') {
          todayBadgeHtml = `<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">🙋 손들기</span>`;
        } else if (student.todayLog === 'called') {
          todayBadgeHtml = `<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30">💬 시켜서</span>`;
        } else if (student.todayLog === 'random') {
          todayBadgeHtml = `<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">🎲 추첨</span>`;
        }

        let pendingBallBadge = '';
        if (pendingBalls > 0) {
          pendingBallBadge = `
            <div class="flex items-center gap-1 px-2 py-0.5 rounded-full bg-rose-500/20 border border-rose-400/60 text-rose-300 font-jua text-[11px] animate-pulse">
              <span class="mini-ball animate-bounce"></span>
              <span>미개봉 ${pendingBalls}개</span>
            </div>
          `;
        }

        const repAvatarHtml = repPoke ? `
          <div class="w-14 h-14 rounded-2xl bg-slate-800/90 border-2 ${tier.border} flex items-center justify-center overflow-hidden flex-shrink-0 relative group-hover:border-emerald-400/60 shadow-sm p-1">
            <img src="${repPoke.imageUrl}" alt="${repPoke.name}" class="w-full h-full object-contain filter drop-shadow" />
            <span class="absolute bottom-0 right-0 text-[9px] px-1 rounded-tl-md ${tier.badgeClass}">
              Lv.${repData.level || 1}
            </span>
          </div>
        ` : `
          <div class="w-14 h-14 rounded-2xl bg-slate-800/60 border-2 border-dashed border-slate-700 flex flex-col items-center justify-center overflow-hidden flex-shrink-0 relative group-hover:border-amber-400/60 shadow-sm" title="대표 포켓몬 미지정">
            <span class="text-xl">❓</span>
            <span class="text-[9px] text-slate-400 font-bold font-jua">미지정</span>
          </div>
        `;

        card.innerHTML = `
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold text-slate-400 group-hover:text-emerald-300 transition">
              ${student.number}번
            </span>
            <div class="flex items-center gap-1.5">
              ${pendingBallBadge}
              ${todayBadgeHtml}
              <span class="text-xs font-bold px-2 py-0.5 rounded-full ${student.count > 0 ? 'bg-amber-400 text-slate-950 font-jua' : 'bg-slate-800 text-slate-400'} border border-amber-400/30">
                발표 ${student.count || 0}회
              </span>
            </div>
          </div>

          <div class="flex items-center gap-3 my-2">
            ${repAvatarHtml}
            <div class="flex-1 min-w-0">
              <h3 class="text-lg font-jua text-white group-hover:text-emerald-300 transition truncate">
                ${student.name}
              </h3>
              <p class="text-xs text-amber-300 font-bold truncate">
                🪙 ${student.happy || 0} 해피
              </p>
              <p class="text-[11px] text-slate-400 truncate">
                수집: <span class="text-emerald-400 font-bold">${collectedCount}</span> / 152종
              </p>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2 mt-2 pt-2 border-t border-slate-800" onclick="event.stopPropagation()">
            <button onclick="teacherQuickAward(${student.id})" class="py-1.5 px-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-jua text-xs shadow transition active:scale-95 flex items-center justify-center gap-1" title="수업 중 발표 즉시 저장 (+1 볼, +15 해피 적립)">
              <span>⚡</span>
              <span>+1 볼 저장</span>
            </button>
            <button onclick="openPokedexForStudent(${student.id})" class="py-1.5 px-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white font-jua text-xs border border-slate-700 transition active:scale-95 flex items-center justify-center gap-1" title="도감 확인">
              <span>📖</span>
              <span>도감 보기</span>
            </button>
          </div>
        `;

        grid.appendChild(card);
      });

      updateGlobalStats();
    }

    function teacherQuickAward(studentId) {
      soundManager.init();
      const student = appState.students.find(s => s.id === studentId);
      if (!student) return;

      const bonus = appState.presentHappyBonus || 15;
      student.count = (student.count || 0) + 1;
      student.pendingBalls = (student.pendingBalls || 0) + 1;
      student.happy = (student.happy || 0) + bonus;
      if (!student.todayLog) student.todayLog = 'called';

      soundManager.playBallAward();
      showToast(`'${student.name}' 학생에게 몬스터볼이 적립되었습니다! (+1 볼, +${bonus} 해피) 🔴`);

      saveState();
      renderStudentGrid();
    }

    function updateGlobalStats() {
      const totalCount = appState.students.reduce((acc, cur) => acc + (cur.count || 0), 0);
      document.getElementById('statTodayCount').textContent = totalCount + '회';

      const uniqueIds = new Set();
      let totalPending = 0;
      appState.students.forEach(s => {
        totalPending += (s.pendingBalls || 0);
        Object.keys(s.collected || {}).forEach(id => uniqueIds.add(id));
      });
      document.getElementById('statTotalCollected').textContent = `${uniqueIds.size} / 152종`;
      document.getElementById('statPendingBallsTotal').textContent = `${totalPending}개`;
    }

    /* ==================== STUDENT PERSONAL VIEW ==================== */
    let activeStudent = null;

    function renderStudentView(studentId) {
      activeStudent = appState.students.find(s => s.id === studentId);
      if (!activeStudent) return;

      const student = activeStudent;
      document.getElementById('studentViewNumberBadge').textContent = `${student.number}번`;
      document.getElementById('studentViewName').textContent = `${student.name}의 포켓몬 연구실`;

      const balls = student.pendingBalls || 0;
      document.getElementById('studentViewBallCount').textContent = `${balls}개`;

      const openBtn = document.getElementById('studentViewOpenBallBtn');
      const noBallMsg = document.getElementById('studentViewNoBallMsg');
      if (balls > 0) {
        openBtn.classList.remove('hidden');
        noBallMsg.classList.add('hidden');
      } else {
        openBtn.classList.add('hidden');
        noBallMsg.classList.remove('hidden');
      }

      // Happy Points
      const happy = student.happy || 0;
      document.getElementById('studentViewHappyTop').textContent = happy;
      document.getElementById('studentViewHappy').textContent = happy;

      // Exchange button state
      const exchangeBtn = document.getElementById('exchangeBallBtn');
      const ballCost = appState.ballExchangeCost || 100;
      exchangeBtn.innerHTML = `
        <span class="mini-ball"></span>
        <span>${ballCost} 해피로 추가 볼 교환! 🎁</span>
      `;
      if (happy >= ballCost) {
        exchangeBtn.className = "px-4 py-2.5 rounded-2xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 active:scale-95 text-slate-950 font-jua text-xs sm:text-sm shadow-md transition flex items-center gap-2 animate-pulse cursor-pointer";
        exchangeBtn.disabled = false;
      } else {
        exchangeBtn.className = "px-4 py-2.5 rounded-2xl bg-slate-800 text-slate-500 font-jua text-xs sm:text-sm border border-slate-700 transition flex items-center gap-2 cursor-not-allowed opacity-80";
        exchangeBtn.disabled = true;
      }

      // Rep Pokemon
      const collectedMap = student.collected || {};
      const collectedCount = Object.keys(collectedMap).length;
      const repId = student.representativePokeId;
      const repPoke = (repId && collectedMap[repId]) ? POKEMON_DATA.find(p => p.id === repId) : null;
      const repData = repPoke ? collectedMap[repId] : null;

      const setBox = document.getElementById('studentRepSetBox');
      const emptyBox = document.getElementById('studentRepEmptyBox');
      const tierBadge = document.getElementById('studentViewTierBadge');
      const trainBtn = document.getElementById('studentTrainingActionBtn');
      const trainBtnText = document.getElementById('studentTrainingActionBtnText');

      if (repPoke && repData) {
        if (setBox) setBox.classList.remove('hidden');
        if (emptyBox) emptyBox.classList.add('hidden');
        if (tierBadge) {
          tierBadge.classList.remove('hidden');
          const tier = getLevelTier(repData.level || 1);
          tierBadge.textContent = `레벨 ${repData.level || 1} · ${tier.name}`;
          tierBadge.className = `text-xs px-2.5 py-0.5 rounded-full font-bold ${tier.badgeClass}`;
        }
        document.getElementById('studentViewRepImg').src = repPoke.imageUrl;
        document.getElementById('studentViewRepName').textContent = repPoke.name;
        document.getElementById('studentViewRepLevel').textContent = `레벨 ${repData.level || 1} • 친밀도 ${repData.friendship || 7}`;

        if (trainBtn) {
          trainBtn.disabled = false;
          trainBtn.className = "w-full mt-4 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 active:scale-95 text-white font-jua text-sm shadow-md transition flex items-center justify-center gap-2 cursor-pointer";
        }
        if (trainBtnText) trainBtnText.textContent = "대표 포켓몬 훈련하기 (-50 해피)";
      } else {
        if (setBox) setBox.classList.add('hidden');
        if (emptyBox) emptyBox.classList.remove('hidden');
        if (tierBadge) tierBadge.classList.add('hidden');

        const emptyDesc = document.getElementById('studentRepEmptyDesc');
        const selectBtn = document.getElementById('studentRepSelectBtn');
        if (collectedCount > 0) {
          if (emptyDesc) emptyDesc.textContent = `현재 보유 중인 포켓몬(${collectedCount}마리) 중에서 대표 포켓몬을 골라보세요!`;
          if (selectBtn) selectBtn.classList.remove('hidden');
        } else {
          if (emptyDesc) emptyDesc.textContent = `아직 수집한 포켓몬이 없어요! 먼저 몬스터볼을 열어 포켓몬을 뽑아보세요.`;
          if (selectBtn) selectBtn.classList.add('hidden');
        }

        if (trainBtn) {
          trainBtn.disabled = true;
          trainBtn.className = "w-full mt-4 py-3 rounded-xl bg-slate-700/50 text-slate-500 font-jua text-sm flex items-center justify-center gap-2 cursor-not-allowed border border-slate-700";
        }
        if (trainBtnText) trainBtnText.textContent = "대표 포켓몬을 먼저 지정해주세요 🔒";
      }

      // Pokedex stats
      const totalPokemon = POKEMON_DATA.length;
      const percent = Math.round((collectedCount / totalPokemon) * 100);
      document.getElementById('studentViewPokedexStats').textContent = `${collectedCount} / ${totalPokemon}종 (${percent}%)`;
      document.getElementById('studentViewProgressBar').style.width = `${percent}%`;
    }

    /* Exchange Happy Points for Extra Monster Ball */
    function exchangeHappyForBall() {
      if (!activeStudent) return;
      const cost = appState.ballExchangeCost || 100;
      if ((activeStudent.happy || 0) < cost) {
        alert(`해피 포인트가 부족합니다. (${cost} 해피 필요)`);
        return;
      }

      activeStudent.happy -= cost;
      activeStudent.pendingBalls = (activeStudent.pendingBalls || 0) + 1;

      soundManager.playLevelUp();
      confetti({
        particleCount: 60,
        spread: 70,
        origin: { y: 0.5 }
      });

      showToast(`🎁 ${cost} 해피로 몬스터볼 1개를 교환했습니다! 지금 바로 뽑아보세요! 🔴`);
      saveState();
      renderStudentView(activeStudent.id);
    }

    function studentOpenBall() {
      if (!activeStudent || (activeStudent.pendingBalls || 0) <= 0) return;
      activeStudent.pendingBalls -= 1;
      saveState();
      renderStudentView(activeStudent.id);
      launchGachaForStudent(activeStudent);
    }

    function openStudentSelfCheckin() {
      if (!activeStudent) return;
      document.getElementById('selfCheckinModal').classList.remove('hidden');
    }
    function closeSelfCheckinModal() {
      document.getElementById('selfCheckinModal').classList.add('hidden');
    }
    function executeStudentSelfCheckin(choiceType) {
      if (!activeStudent) return;
      closeSelfCheckinModal();

      const bonus = choiceType === 'voluntary' 
        ? (appState.presentHappyBonus || 15) 
        : Math.max(10, (appState.presentHappyBonus || 15) - 5);

      activeStudent.count = (activeStudent.count || 0) + 1;
      activeStudent.pendingBalls = (activeStudent.pendingBalls || 0) + 1;
      activeStudent.happy = (activeStudent.happy || 0) + bonus;
      activeStudent.todayLog = choiceType;

      soundManager.playBallAward();
      saveState();
      renderStudentView(activeStudent.id);
      showToast(`발표가 등록되어 몬스터볼 1개(+${bonus} 해피)를 받았습니다! 🔴`);
    }

    function openTrainingForCurrentStudentView() {
      if (activeStudent) {
        openTrainingModalForStudent(activeStudent.id);
      }
    }

    function openPokedexForCurrentStudentView() {
      if (activeStudent) {
        openPokedexForStudent(activeStudent.id);
      }
    }

    /* ==================== GACHA FLOW ==================== */
    let currentGachaStudent = null;
    let pendingPokemon = null;
    let gachaTimer = null;

    function getRandomPokemon() {
      const rand = Math.random() * 100;
      let targetRarity = '일반';
      if (rand < 5) {
        targetRarity = '전설';
      } else if (rand < 30) {
        targetRarity = '희귀';
      } else {
        targetRarity = '일반';
      }

      const pool = POKEMON_DATA.filter(p => p.rarity === targetRarity);
      if (pool.length === 0) return POKEMON_DATA[Math.floor(Math.random() * POKEMON_DATA.length)];
      return pool[Math.floor(Math.random() * pool.length)];
    }

    function launchGachaForStudent(student) {
      currentGachaStudent = student;
      pendingPokemon = getRandomPokemon();

      document.getElementById('gachaStudentName').textContent = currentGachaStudent.name;
      document.getElementById('ballStage').classList.remove('hidden');
      document.getElementById('cardStage').classList.add('hidden');
      document.getElementById('gachaModal').classList.remove('hidden');

      const ball = document.getElementById('wigglingBall');
      ball.className = "w-36 h-36 sm:w-44 sm:h-44 rounded-full pokeball-btn shadow-2xl animate-ball-wiggle cursor-pointer transition-transform";

      soundManager.playTick();
      setTimeout(() => soundManager.playTick(), 600);
      setTimeout(() => soundManager.playTick(), 1200);

      if (gachaTimer) clearTimeout(gachaTimer);
      gachaTimer = setTimeout(() => {
        triggerOpenBall();
      }, 1800);
    }

    function triggerOpenBall() {
      if (gachaTimer) clearTimeout(gachaTimer);
      if (!currentGachaStudent || !pendingPokemon) return;

      soundManager.playOpenBall();

      const now = new Date();
      const dateStr = `${now.getFullYear()}. ${now.getMonth() + 1}. ${now.getDate()}.`;
      
      if (!currentGachaStudent.collected) {
        currentGachaStudent.collected = {};
      }

      const pokeId = pendingPokemon.id;
      if (!currentGachaStudent.collected[pokeId]) {
        currentGachaStudent.collected[pokeId] = {
          count: 1,
          firstMet: dateStr,
          level: 2,
          exp: 10,
          friendship: 7
        };
      } else {
        currentGachaStudent.collected[pokeId].count += 1;
        currentGachaStudent.collected[pokeId].friendship = (currentGachaStudent.collected[pokeId].friendship || 7) + 1;
        currentGachaStudent.collected[pokeId].exp = ((currentGachaStudent.collected[pokeId].exp || 0) + 10) % 30;
      }

      // Do not auto-assign representative pokemon; let student choose!
      saveState();
      if (appState.currentSession && appState.currentSession.role === 'student') {
        renderStudentView(currentGachaStudent.id);
      } else {
        renderStudentGrid();
      }

      updateRewardSetRepButton();

      const pokeRecord = currentGachaStudent.collected[pokeId];
      document.getElementById('rewardPokemonName').textContent = pendingPokemon.name;
      document.getElementById('rewardPokemonImage').src = pendingPokemon.imageUrl;
      document.getElementById('rewardFirstMetDate').textContent = `처음 만난 날 · ${pokeRecord.firstMet}`;
      document.getElementById('rewardMetCount').textContent = `${pokeRecord.count}번 만났어요`;
      document.getElementById('rewardLevelFriendship').textContent = `포켓몬 레벨 ${pokeRecord.level || 2} · 친밀도 ${pokeRecord.friendship || 7}`;
      document.getElementById('rewardStudentBadge').textContent = currentGachaStudent.name;

      const cardContainer = document.getElementById('rewardCardContainer');
      const badge = document.getElementById('rewardRarityBadge');
      
      cardContainer.className = "w-full rounded-3xl p-6 sm:p-7 relative transition-all duration-300 animate-card-pop text-slate-900 border-4 shadow-2xl flex flex-col items-center ";
      if (pendingPokemon.rarity === '전설') {
        cardContainer.classList.add('holo-card-legendary', 'border-amber-400');
        badge.className = "text-xs font-bold px-3 py-1 rounded-full bg-amber-500 text-slate-950 tracking-wider shadow animate-pulse";
        badge.textContent = "전설";
      } else if (pendingPokemon.rarity === '희귀') {
        cardContainer.classList.add('holo-card-rare', 'border-purple-400');
        badge.className = "text-xs font-bold px-3 py-0.5 rounded-full bg-purple-600 text-white tracking-wider";
        badge.textContent = "매우 희귀";
      } else {
        cardContainer.classList.add('holo-card', 'border-amber-300');
        badge.className = "text-xs font-bold px-3 py-0.5 rounded-full bg-slate-800/10 text-slate-700 tracking-wider";
        badge.textContent = "일반";
      }

      document.getElementById('ballStage').classList.add('hidden');
      document.getElementById('cardStage').classList.remove('hidden');

      setTimeout(() => {
        soundManager.playFanfare(pendingPokemon.rarity === '전설');
        confetti({
          particleCount: pendingPokemon.rarity === '전설' ? 120 : 60,
          spread: 70,
          origin: { y: 0.6 }
        });
      }, 100);
    }

    function setRepFromReward() {
      if (!currentGachaStudent || !pendingPokemon) return;
      currentGachaStudent.representativePokeId = pendingPokemon.id;
      saveState();
      if (appState.currentSession && appState.currentSession.role === 'student') {
        renderStudentView(currentGachaStudent.id);
      } else {
        renderStudentGrid();
      }
      soundManager.playLevelUp();
      confetti({
        particleCount: 50,
        spread: 60,
        origin: { y: 0.6 }
      });
      updateRewardSetRepButton();
      showToast(`'${pendingPokemon.name}'(이)가 나의 대표 포켓몬으로 지정되었습니다! 👑`);
    }

    function updateRewardSetRepButton() {
      if (!currentGachaStudent || !pendingPokemon) return;
      const btn = document.getElementById('rewardSetRepBtn');
      const txt = document.getElementById('rewardSetRepText');
      if (!btn || !txt) return;

      if (currentGachaStudent.representativePokeId === pendingPokemon.id) {
        btn.className = "w-full mt-4 py-2.5 rounded-2xl bg-amber-600/30 border border-amber-600/40 text-amber-950 font-jua text-sm flex items-center justify-center gap-1.5 cursor-default";
        txt.textContent = "👑 현재 나의 대표 포켓몬입니다!";
        btn.onclick = null;
      } else {
        btn.className = "w-full mt-4 py-2.5 rounded-2xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-slate-950 font-jua text-sm shadow-md transition active:scale-95 flex items-center justify-center gap-1.5 cursor-pointer";
        txt.textContent = "👑 이 포켓몬을 대표 포켓몬으로 설정하기";
        btn.onclick = setRepFromReward;
      }
    }

    function closeGachaModal() {
      document.getElementById('gachaModal').classList.add('hidden');
      if (gachaTimer) clearTimeout(gachaTimer);
      currentGachaStudent = null;
      pendingPokemon = null;
    }

    function goToPokedexFromGacha() {
      const studentId = currentGachaStudent ? currentGachaStudent.id : null;
      closeGachaModal();
      if (studentId) {
        openPokedexForStudent(studentId);
        filterPokedex('collected');
      }
    }

    /* ==================== TRAINING LOGIC ==================== */
    let activeTrainingStudent = null;

    function openTrainingForCurrentStudentView() {
      if (!activeStudent) return;
      const collectedMap = activeStudent.collected || {};
      const repId = activeStudent.representativePokeId;
      if (!repId || !collectedMap[repId]) {
        showToast('먼저 도감에서 대표 포켓몬을 지정해주세요! 👑');
        openPokedexForCurrentStudentView();
        return;
      }
      openTrainingModalForStudent(activeStudent.id);
    }

    function openTrainingModalForStudent(studentId) {
      soundManager.init();
      activeTrainingStudent = appState.students.find(s => s.id === studentId);
      if (!activeTrainingStudent) return;

      const student = activeTrainingStudent;
      const collectedMap = student.collected || {};
      const repId = student.representativePokeId;
      if (!repId || !collectedMap[repId]) {
        showToast('먼저 도감에서 대표 포켓몬을 지정해주세요! 👑');
        openPokedexForStudent(student.id);
        return;
      }

      const repPoke = POKEMON_DATA.find(p => p.id === repId);
      if (!repPoke) return;
      const repData = collectedMap[repId] || { level: 2, exp: 0, friendship: 7 };

      document.getElementById('trainingHappyPoints').textContent = student.happy || 0;
      document.getElementById('trainingPokeImg').src = repPoke.imageUrl;
      document.getElementById('trainingPokeName').textContent = repPoke.name;
      
      const tier = getLevelTier(repData.level || 1);
      document.getElementById('trainingPokeLevelBadge').textContent = `레벨 ${repData.level || 1} · ${tier.name}`;

      const btn = document.getElementById('trainingActionBtn');
      if (student.trainedToday) {
        btn.textContent = "오늘 훈련 완료 또는 모두 챔피언";
        btn.disabled = true;
        btn.className = "w-full py-3 rounded-2xl bg-slate-200 text-slate-500 font-jua text-sm sm:text-base cursor-not-allowed";
      } else if ((student.happy || 0) < 50) {
        btn.textContent = "해피 포인트 부족 (50 해피 필요)";
        btn.disabled = true;
        btn.className = "w-full py-3 rounded-2xl bg-slate-200 text-slate-500 font-jua text-sm sm:text-base cursor-not-allowed";
      } else if ((repData.level || 1) >= 5) {
        btn.textContent = "이미 최고 레벨(챔피언)입니다!";
        btn.disabled = true;
        btn.className = "w-full py-3 rounded-2xl bg-amber-400 text-slate-900 font-jua text-sm sm:text-base cursor-not-allowed";
      } else {
        btn.textContent = "훈련하기 (-50 해피, 레벨 +1)";
        btn.disabled = false;
        btn.className = "w-full py-3 rounded-2xl bg-[#00897b] hover:bg-[#00796b] active:scale-95 text-white font-jua text-sm sm:text-base shadow-md transition";
      }

      document.getElementById('trainingModal').classList.remove('hidden');
    }

    function closeTrainingModal() {
      document.getElementById('trainingModal').classList.add('hidden');
      activeTrainingStudent = null;
    }

    function executeTraining() {
      if (!activeTrainingStudent) return;
      const student = activeTrainingStudent;
      const repId = student.representativePokeId;
      if (!repId || !student.collected || !student.collected[repId]) return;

      if ((student.happy || 0) < 50 || student.trainedToday) return;

      student.happy -= 50;
      student.trainedToday = true;

      if (!student.collected) student.collected = {};
      if (!student.collected[repId]) {
        student.collected[repId] = {
          count: 1,
          firstMet: new Date().toISOString().split('T')[0],
          level: 2,
          exp: 0,
          friendship: 7
        };
      }

      student.collected[repId].level = Math.min(5, (student.collected[repId].level || 1) + 1);
      student.collected[repId].friendship = (student.collected[repId].friendship || 7) + 3;

      soundManager.playLevelUp();
      confetti({
        particleCount: 50,
        spread: 60,
        origin: { y: 0.6 }
      });

      saveState();
      if (appState.currentSession && appState.currentSession.role === 'student') {
        renderStudentView(student.id);
      } else {
        renderStudentGrid();
      }
      openTrainingModalForStudent(student.id);
    }

    /* ==================== POKEDEX MODAL ==================== */
    let currentPokedexStudent = null;
    let pokedexFilter = 'all';

    function openPokedexForStudent(studentId) {
      currentPokedexStudent = appState.students.find(s => s.id === studentId);
      if (!currentPokedexStudent) return;

      document.getElementById('pokedexStudentName').textContent = currentPokedexStudent.name;
      pokedexFilter = 'all';
      renderPokedexView();
      document.getElementById('pokedexModal').classList.remove('hidden');
    }

    function closePokedexModal() {
      document.getElementById('pokedexModal').classList.add('hidden');
      currentPokedexStudent = null;
    }

    function filterPokedex(filter) {
      pokedexFilter = filter;
      ['All', 'Collected', 'Uncollected'].forEach(t => {
        const btn = document.getElementById('filterTab' + t);
        if (t.toLowerCase() === filter) {
          btn.className = "px-2.5 py-1 rounded-lg bg-amber-500 text-slate-900 font-bold transition";
        } else {
          btn.className = "px-2.5 py-1 rounded-lg text-slate-300 hover:text-white transition";
        }
      });
      renderPokedexView();
    }

    function setRepresentativePokemon(pokeId) {
      if (!currentPokedexStudent) return;
      currentPokedexStudent.representativePokeId = pokeId;
      saveState();
      if (appState.currentSession && appState.currentSession.role === 'student') {
        renderStudentView(currentPokedexStudent.id);
      } else {
        renderStudentGrid();
      }
      renderPokedexView();
      soundManager.playLevelUp();
      confetti({ particleCount: 50, spread: 60, origin: { y: 0.6 } });
      const poke = POKEMON_DATA.find(p => p.id === pokeId);
      showToast(`'${poke ? poke.name : '포켓몬'}'(이)가 나의 대표 포켓몬으로 지정되었습니다! 👑`);
    }

    function renderPokedexView() {
      if (!currentPokedexStudent) return;
      const student = currentPokedexStudent;
      const collectedMap = student.collected || {};
      const collectedCount = Object.keys(collectedMap).length;
      const totalPokemon = POKEMON_DATA.length;
      const percent = Math.round((collectedCount / totalPokemon) * 100);

      document.getElementById('pokedexStudentStats').textContent = 
        `발표 ${student.count || 0}회 • 수집 ${collectedCount} / ${totalPokemon}종 (${percent}%) • 🪙 ${student.happy || 0} 해피`;
      document.getElementById('pokedexPercentText').textContent = percent + '%';
      document.getElementById('pokedexProgressBar').style.width = percent + '%';

      const grid = document.getElementById('pokedexGrid');
      grid.innerHTML = '';

      POKEMON_DATA.forEach(poke => {
        const isCollected = !!collectedMap[poke.id];

        if (pokedexFilter === 'collected' && !isCollected) return;
        if (pokedexFilter === 'uncollected' && isCollected) return;

        const record = collectedMap[poke.id] || { count: 0, firstMet: '', level: 2, exp: 0 };
        const isRep = student.representativePokeId === poke.id;
        const formattedNum = String(poke.id).padStart(3, '0');

        const card = document.createElement('div');
        
        if (isCollected) {
          card.className = "rounded-3xl p-4 bg-[#fef08a] border-2 " + (isRep ? "border-amber-500 ring-2 ring-amber-400 shadow-xl" : "border-amber-300 shadow-md") + " flex flex-col justify-between text-slate-900 cursor-pointer hover:shadow-xl transition-all duration-200 relative";
          card.onclick = () => setRepresentativePokemon(poke.id);

          card.innerHTML = `
            <div class="flex items-center justify-between text-xs font-bold text-slate-800 mb-1">
              <span class="font-mono">도감 ${formattedNum}</span>
              <div class="flex items-center gap-1">
                ${isRep ? `<span class="bg-amber-500 text-slate-950 text-[10px] px-1.5 py-0.5 rounded-full font-jua font-bold">👑 대표</span>` : ''}
                <span class="text-emerald-700 text-sm font-black">✓</span>
              </div>
            </div>

            <div class="text-center my-0.5">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-900/10 text-slate-700">
                ${poke.rarity === '전설' ? '전설' : poke.rarity === '희귀' ? '매우 희귀' : '일반'}
              </span>
            </div>

            <div class="w-24 h-24 sm:w-28 sm:h-28 mx-auto my-1 flex items-center justify-center">
              <img src="${poke.imageUrl}" alt="${poke.name}" class="w-full h-full object-contain filter drop-shadow-md" loading="lazy" />
            </div>

            <div class="text-center">
              <h4 class="text-base sm:text-lg font-jua text-slate-900 leading-tight">
                ${poke.name}
              </h4>
              <p class="text-[11px] text-slate-700 font-medium mt-0.5">
                ${record.count}번의 만남
              </p>
              <p class="text-[10px] text-slate-600">
                획득 ${record.firstMet || '-'}
              </p>
            </div>

            <div class="mt-2 pt-2 border-t border-slate-900/10 text-center">
              <div class="flex justify-between text-[10px] font-bold text-slate-800 mb-0.5">
                <span>레벨 ${record.level || 2}</span>
                <span>${record.exp || 0} / 30 경험치</span>
              </div>
              <div class="w-full h-1.5 bg-slate-900/20 rounded-full overflow-hidden">
                <div class="h-full bg-amber-600 rounded-full" style="width: ${Math.min(100, ((record.exp || 0) / 30) * 100)}%"></div>
              </div>
            </div>

            <button onclick="event.stopPropagation(); setRepresentativePokemon(${poke.id});" class="mt-2.5 w-full py-1.5 px-2 rounded-xl text-xs font-jua transition flex items-center justify-center gap-1 ${isRep ? 'bg-amber-500 text-slate-950 font-bold shadow' : 'bg-slate-900/10 hover:bg-slate-900/20 text-slate-800 cursor-pointer'}">
              <span>${isRep ? '👑' : '⭐'}</span>
              <span>${isRep ? '나의 대표 포켓몬' : '대표 포켓몬으로 설정'}</span>
            </button>
          `;
        } else {
          card.className = "rounded-3xl p-4 bg-[#fbf8ee] border-2 border-slate-200/80 shadow-sm flex flex-col justify-between text-slate-800 opacity-90 relative";
          
          card.innerHTML = `
            <div class="flex items-center justify-between text-xs font-bold text-slate-600 mb-1">
              <span class="font-mono">도감 ${formattedNum}</span>
            </div>

            <div class="text-center my-0.5">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-200 text-slate-600">
                ${poke.rarity === '전설' ? '전설' : poke.rarity === '희귀' ? '매우 희귀' : '일반'}
              </span>
            </div>

            <div class="w-24 h-24 sm:w-28 sm:h-28 mx-auto my-1 flex items-center justify-center relative">
              <img src="${poke.imageUrl}" alt="미발견" class="w-full h-full object-contain filter brightness-0 contrast-50 opacity-20" loading="lazy" />
              <span class="absolute inset-0 flex items-center justify-center font-jua text-2xl text-slate-400">?</span>
            </div>

            <div class="text-center">
              <h4 class="text-sm sm:text-base font-jua text-slate-700 leading-tight">
                미발견 포켓몬
              </h4>
              <p class="text-[11px] text-slate-500 mt-0.5">
                새로운 만남을 기다려요
              </p>
            </div>

            <div class="mt-2 pt-2 border-t border-slate-200 text-center">
              <span class="text-[10px] text-slate-400 font-medium">발견 가능</span>
            </div>
          `;
        }

        grid.appendChild(card);
      });
    }

    /* ==================== ROULETTE LOGIC ==================== */
    let rouletteTimer = null;
    let rouletteWinner = null;

    function openRouletteModal() {
      rouletteWinner = null;
      document.getElementById('rouletteNumberBadge').textContent = '번호 대기중';
      document.getElementById('rouletteNameDisplay').textContent = '준비 완료!';
      document.getElementById('rouletteInitialBtns').classList.remove('hidden');
      document.getElementById('rouletteWinnerBtns').classList.add('hidden');
      document.getElementById('rouletteModal').classList.remove('hidden');
    }
    function closeRouletteModal() {
      if (rouletteTimer) clearInterval(rouletteTimer);
      document.getElementById('rouletteModal').classList.add('hidden');
    }

    function startRouletteSpin() {
      soundManager.init();
      if (appState.students.length === 0) return;

      const initialBtns = document.getElementById('rouletteInitialBtns');
      const winnerBtns = document.getElementById('rouletteWinnerBtns');
      initialBtns.classList.add('opacity-50', 'pointer-events-none');

      let speed = 50;
      let elapsed = 0;
      const totalTime = 2500;
      let currentIndex = 0;

      function spinStep() {
        currentIndex = (currentIndex + 1) % appState.students.length;
        const currentStudent = appState.students[currentIndex];
        
        document.getElementById('rouletteNumberBadge').textContent = `${currentStudent.number}번`;
        document.getElementById('rouletteNameDisplay').textContent = currentStudent.name;
        soundManager.playTick();

        elapsed += speed;
        if (elapsed < totalTime) {
          speed = Math.floor(50 + (elapsed / totalTime) * 200);
          setTimeout(spinStep, speed);
        } else {
          const winnerIndex = Math.floor(Math.random() * appState.students.length);
          rouletteWinner = appState.students[winnerIndex];
          document.getElementById('rouletteNumberBadge').textContent = `🎉 ${rouletteWinner.number}번 당첨!`;
          document.getElementById('rouletteNameDisplay').textContent = rouletteWinner.name;
          soundManager.playWinJingle();

          confetti({
            particleCount: 50,
            spread: 60,
            origin: { y: 0.5 }
          });

          initialBtns.classList.add('hidden');
          initialBtns.classList.remove('opacity-50', 'pointer-events-none');
          winnerBtns.classList.remove('hidden');
        }
      }

      spinStep();
    }

    function saveWinnerBallOnly() {
      if (!rouletteWinner) return;
      const winner = rouletteWinner;
      closeRouletteModal();
      
      const bonus = appState.presentHappyBonus || 15;
      winner.count = (winner.count || 0) + 1;
      winner.pendingBalls = (winner.pendingBalls || 0) + 1;
      winner.happy = (winner.happy || 0) + bonus;
      winner.todayLog = 'random';

      soundManager.playBallAward();
      saveState();
      renderStudentGrid();
      showToast(`'${winner.name}' 학생에게 몬스터볼이 저장되었습니다! (+1 볼, +${bonus} 해피) 🔴`);
    }

    function openWinnerGachaNow() {
      if (!rouletteWinner) return;
      const winner = rouletteWinner;
      closeRouletteModal();

      const bonus = appState.presentHappyBonus || 15;
      winner.count = (winner.count || 0) + 1;
      winner.happy = (winner.happy || 0) + bonus;
      winner.todayLog = 'random';

      saveState();
      renderStudentGrid();
      launchGachaForStudent(winner);
    }

    /* ==================== SETTINGS & MANAGEMENT ==================== */
    function updateSettingsInputs() {
      const d = document.getElementById('settingDailyHappy');
      const p = document.getElementById('settingPresentHappy');
      const b = document.getElementById('settingBallCost');
      if (d) d.value = appState.dailyHappyBonus || 20;
      if (p) p.value = appState.presentHappyBonus || 15;
      if (b) b.value = appState.ballExchangeCost || 100;

      const cid = document.getElementById('settingClassId');
      const fcfg = document.getElementById('settingFirebaseConfig');
      if (cid) cid.value = appState.classId || 'classroom_5_default';
      if (fcfg) {
        fcfg.value = appState.firebaseConfig ? JSON.stringify(appState.firebaseConfig, null, 2) : '';
      }
      updateCloudStatusUI(!!(firestoreDb && appState.firebaseConfig));
    }

    function saveEconomySettings() {
      const d = parseInt(document.getElementById('settingDailyHappy').value) || 20;
      const p = parseInt(document.getElementById('settingPresentHappy').value) || 15;
      const b = parseInt(document.getElementById('settingBallCost').value) || 100;

      appState.dailyHappyBonus = d;
      appState.presentHappyBonus = p;
      appState.ballExchangeCost = b;
      saveState();
      alert('포인트 및 볼 교환 규칙이 성공적으로 저장되었습니다!');
    }

    function openClassSettings() {
      const newName = prompt('학급 명칭을 입력하세요:', appState.className);
      if (newName && newName.trim()) {
        appState.className = newName.trim();
        saveState();
        renderStudentGrid();
      }
    }

    function changeTeacherPasswordPrompt() {
      const newPw = prompt('새로운 선생님 비밀번호를 입력하세요:', appState.teacherPassword);
      if (newPw && newPw.trim()) {
        appState.teacherPassword = newPw.trim();
        saveState();
        alert('선생님 비밀번호가 성공적으로 변경되었습니다!');
      }
    }

    function openManageModal() {
      updateSettingsInputs();
      renderManageStudentList();
      document.getElementById('manageModal').classList.remove('hidden');
    }
    function closeManageModal() {
      document.getElementById('manageModal').classList.add('hidden');
    }

    function renderManageStudentList() {
      const container = document.getElementById('manageStudentList');
      container.innerHTML = '';
      document.getElementById('manageStudentCount').textContent = appState.students.length;

      appState.students.forEach((student) => {
        const row = document.createElement('div');
        row.className = "flex items-center justify-between p-3 hover:bg-slate-800/60 transition gap-2 flex-wrap";
        const repId = student.representativePokeId;
        const repName = (repId && student.collected && student.collected[repId]) 
          ? (POKEMON_DATA.find(p => p.id === repId)?.name || '지정됨') 
          : '미지정';

        row.innerHTML = `
          <div class="flex items-center gap-3">
            <span class="text-xs font-mono text-slate-400 w-8">${student.number}번</span>
            <span class="font-jua text-white text-base">${student.name}</span>
            <span class="text-xs text-amber-300 font-mono bg-slate-800 px-2 py-0.5 rounded border border-slate-700">비번: ${student.password || '0000'}</span>
            <span class="text-xs text-slate-400">(발표 ${student.count || 0}회, 🪙 ${student.happy || 0} 해피, 🔴 볼 ${student.pendingBalls || 0}개, 👑 대표: ${repName})</span>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="editStudentPasswordPrompt(${student.id})" class="text-xs text-amber-300 hover:text-amber-200 bg-slate-800 px-2 py-1 rounded transition">비번 수정</button>
            <button onclick="editStudentPrompt(${student.id})" class="text-xs text-slate-300 hover:text-white bg-slate-800 px-2 py-1 rounded transition">이름 수정</button>
            <button onclick="deleteStudent(${student.id})" class="text-xs text-red-400 hover:text-red-300 bg-slate-800 px-2 py-1 rounded transition">삭제</button>
          </div>
        `;
        container.appendChild(row);
      });
    }

    function editStudentPasswordPrompt(studentId) {
      const student = appState.students.find(s => s.id === studentId);
      if (!student) return;
      const newPw = prompt(`'${student.name}' 학생의 새 비밀번호를 입력하세요:`, student.password);
      if (newPw && newPw.trim()) {
        student.password = newPw.trim();
        saveState();
        renderManageStudentList();
      }
    }

    function addNewStudentPrompt() {
      const name = prompt('추가할 학생의 이름을 입력하세요:');
      if (!name || !name.trim()) return;
      const nextNum = appState.students.length > 0 
        ? Math.max(...appState.students.map(s => s.number || 0)) + 1 
        : 1;
      const nextId = appState.students.length > 0 
        ? Math.max(...appState.students.map(s => s.id || 0)) + 1 
        : 1;
      
      appState.students.push({
        id: nextId,
        number: nextNum,
        name: name.trim(),
        password: String(nextNum).padStart(4, '0'),
        count: 0,
        happy: 150,
        pendingBalls: 0,
        representativePokeId: null,
        todayLog: null,
        lastAttendance: "",
        trainedToday: false,
        collected: {}
      });

      saveState();
      renderStudentGrid();
      renderManageStudentList();
      populateLoginStudentDropdown();
    }

    function editStudentPrompt(studentId) {
      const student = appState.students.find(s => s.id === studentId);
      if (!student) return;
      const newName = prompt(`'${student.name}' 학생의 새 이름을 입력하세요:`, student.name);
      if (!newName || !newName.trim()) return;
      student.name = newName.trim();
      saveState();
      renderStudentGrid();
      renderManageStudentList();
      populateLoginStudentDropdown();
    }

    function deleteStudent(studentId) {
      const student = appState.students.find(s => s.id === studentId);
      if (!student) return;
      if (!confirm(`'${student.name}' 학생을 명단에서 삭제하시겠습니까? (수집 기록도 함께 삭제됩니다)`)) return;
      appState.students = appState.students.filter(s => s.id !== studentId);
      saveState();
      renderStudentGrid();
      renderManageStudentList();
      populateLoginStudentDropdown();
    }

    function exportData() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(appState, null, 2));
      const downloadAnchor = document.createElement('a');
      const filename = `우리반_포켓몬발표도감_${new Date().toISOString().slice(0, 10)}.json`;
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", filename);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    }

    function importData(event) {
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const imported = JSON.parse(e.target.result);
          if (imported && Array.isArray(imported.students)) {
            appState = imported;
            saveState();
            renderStudentGrid();
            renderManageStudentList();
            populateLoginStudentDropdown();
            updateSettingsInputs();
            alert('데이터가 성공적으로 복원되었습니다! 🎉');
          } else {
            alert('올바른 백업 파일 형식이 아닙니다.');
          }
        } catch (err) {
          alert('파일을 읽는 도중 오류가 발생했습니다: ' + err.message);
        }
      };
      reader.readAsText(file);
      event.target.value = '';
    }

    function resetAllDataConfirm() {
      if (confirm('정말로 모든 발표 기록과 도감 수집 데이터를 0으로 초기화하시겠습니까?\\n(학생 명단 및 비밀번호는 유지됩니다)')) {
        appState.students.forEach(s => {
          s.count = 0;
          s.happy = 150;
          s.pendingBalls = 0;
          s.representativePokeId = null;
          s.todayLog = null;
          s.lastAttendance = "";
          s.trainedToday = false;
          s.collected = {};
        });
        saveState();
        renderStudentGrid();
        renderManageStudentList();
        alert('모든 발표 및 도감 기록이 초기화되었습니다.');
      }
    }

    window.addEventListener('DOMContentLoaded', () => {
      loadState();
    });
  </script>
</body>
</html>
"""

final_html = html_template.replace('__POKEMON_DATA_JSON__', json.dumps(pokemon_data, ensure_ascii=False))
final_html = final_html.replace('__INITIAL_STUDENTS_JSON__', json.dumps(initial_students, ensure_ascii=False))

with open('/Users/macbook/Documents/antigravity/pocketmon/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Successfully rebuilt index.html with Happy Points Economy & Ball Exchange! File size:', len(final_html))
