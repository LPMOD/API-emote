import requests, os, psutil, sys, jwt, pickle, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp, asyncio
from fastapi import FastAPI, Query, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import *
from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, sQ_pb2, Team_msg_pb2
from cfonts import render, say
import uvicorn

# EMOTES BY YASH X CODEX - CONVERTED TO FASTAPI

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Global Variables
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False

# FastAPI App
app = FastAPI(
    title="Free Fire Emote Bot API",
    description="Ultra Fast Emote Bot with FastAPI",
    version="2.0.0"
)

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB51"
}

def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200:
                return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.118.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto

async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9:
        headers = '0000000'
    elif uid_length == 8:
        headers = '00000000'
    elif uid_length == 10:
        headers = '000000'
    elif uid_length == 11:
        headers = '00000'
    login_packet = f"9ca8f4{headers}{uid_hex}0700{encrypted_packet_length}00{encrypted_packet}{encrypted_timestamp}"
    return login_packet

async def TcPOnLine(ip, port, key, iv, AutHToKen):
    global online_writer
    reconnect_delay = 5
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            xAuthHeader = bytes.fromhex(AutHToKen)
            await SEndPacKeT(None, online_writer, 'OnLine', xAuthHeader)
            while True:
                packet = await ReaD_PacKeT(reader)
                if not packet:
                    break
            online_writer = None
        except Exception as e:
            print(f"ErroR OnLine {ip}:{port} - {e}")
            online_writer = None
        await asyncio.sleep(reconnect_delay)

async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region):
    global whisper_writer, online_writer, BOT_UID
    reconnect_delay = 5
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            xAuthHeader = bytes.fromhex(AutHToKen)
            await SEndPacKeT(whisper_writer, None, 'ChaT', xAuthHeader)
            ready_event.set()
            
            while True:
                packet = await ReaD_PacKeT(reader)
                if not packet:
                    break
                response = await DecoDe_PacKeT(packet, key, iv, LoGinDaTaUncRypTinG)
                
                if response and response.Data.msgT == 0:
                    try:
                        inPuTMsG = response.Data.Message.strip().lower()
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        
                        if inPuTMsG.startswith("/d "):
                            try:
                                parts = inPuTMsG.split()
                                idT = int(parts[-1])
                                uids = [int(x) for x in parts[1:-1]]
                                
                                for target_uid in uids:
                                    H = await Emote_k(target_uid, idT, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                            except Exception as e:
                                pass
                        
                        elif inPuTMsG.startswith("/f "):
                            try:
                                parts = inPuTMsG.split()
                                idT = int(parts[-1])
                                
                                uid1 = int(parts[1]) if len(parts) > 2 else None
                                uid2 = int(parts[2]) if len(parts) > 3 else None
                                uid3 = int(parts[3]) if len(parts) > 4 else None
                                uid4 = int(parts[4]) if len(parts) > 5 else None
                                uid5 = int(parts[5]) if len(parts) > 6 else None
                                uid6 = int(parts[6]) if len(parts) > 7 else None
                                
                                for target in [uid1, uid2, uid3, uid4, uid5, uid6]:
                                    if target:
                                        H = await Emote_k(target, idT, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                            except Exception as e:
                                pass
                        
                        if inPuTMsG in ("dev"):
                            message = '/d <uid1> <uid2>... <emoteid> /f <uid1> <uid2>... <emoteid> for fast emote'
                            P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        response = None
                    except Exception as e:
                        pass
            
            whisper_writer.close()
            await whisper_writer.wait_closed()
            whisper_writer = None
        
        except Exception as e:
            print(f"ErroR {ip}:{port} - {e}")
            whisper_writer = None
        await asyncio.sleep(reconnect_delay)

loop = None

async def perform_emote(team_code: str, uids: list, emote_id: int):
    global key, iv, region, online_writer, BOT_UID
    
    if online_writer is None:
        raise Exception("Bot not connected")
    
    try:
        EM = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(None, online_writer, 'OnLine', EM)
        await asyncio.sleep(0.10)
        
        for uid_str in uids:
            uid = int(uid_str)
            H = await Emote_k(uid, emote_id, key, iv, region)
            await SEndPacKeT(None, online_writer, 'OnLine', H)
        
        LV = await ExiT(BOT_UID, key, iv)
        await SEndPacKeT(None, online_writer, 'OnLine', LV)
        await asyncio.sleep(0.03)
        
        return {"status": "success", "message": "Emote done & bot left instantly"}
    
    except Exception as e:
        raise Exception(f"Failed to perform emote: {str(e)}")

# ===================== FASTAPI ROUTES =====================

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Free Fire Emote Bot API - FastAPI v2.0",
        "docs": "/docs",
        "bot_status": "connected" if online_writer else "disconnected"
    }

@app.get("/status")
async def status():
    return {
        "bot_connected": online_writer is not None,
        "chat_connected": whisper_writer is not None,
        "version": "2.0.0 FastAPI"
    }

@app.get("/join")
async def join_team(
    tc: str = Query(..., description="Team Code"),
    emote_id: str = Query(..., description="Emote ID"),
    uid1: str = Query(None, description="User ID 1"),
    uid2: str = Query(None, description="User ID 2"),
    uid3: str = Query(None, description="User ID 3"),
    uid4: str = Query(None, description="User ID 4"),
    uid5: str = Query(None, description="User ID 5"),
    uid6: str = Query(None, description="User ID 6")
):
    global loop
    
    if not tc or not emote_id:
        raise HTTPException(status_code=400, detail="Missing tc or emote_id")
    
    try:
        emote_id_int = int(emote_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="emote_id must be integer")
    
    uids = [uid for uid in [uid1, uid2, uid3, uid4, uid5, uid6] if uid]
    
    if not uids:
        raise HTTPException(status_code=400, detail="Provide at least one UID")
    
    if loop is None:
        raise HTTPException(status_code=503, detail="Bot is not initialized")
    
    if online_writer is None:
        raise HTTPException(status_code=503, detail="Bot not connected")
    
    asyncio.run_coroutine_threadsafe(
        perform_emote(tc, uids, emote_id_int), loop
    )
    
    return {
        "status": "success",
        "team_code": tc,
        "uids": uids,
        "emote_id": emote_id,
        "message": "Emote triggered - Ultra Fast Mode"
    }

# ===================== MAIN BOT SYSTEM =====================

async def MaiiiinE():
    global loop, key, iv, region, BOT_UID
    
    BOT_UID = int('1482210279')
    Uid, Pw = '4354560153', 'B99FF557D608F087B48589CBDA09EC2B878636762E59235D661D0C6692DF11FD'
    
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token:
        print("ErroR - InvaLid AccounT")
        return None
    
    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print("TarGeT AccounT => BannEd / NoT ReGisTeReD !")
        return None
    
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    print(UrL)
    region = MajoRLoGinauTh.region
    
    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    loop = asyncio.get_running_loop()
    
    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa:
        print("ErroR - GeTinG PorTs From LoGin DaTa !")
        return None
    
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    
    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")
    
    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(ToKen)
    
    equie_emote(ToKen, UrL)
    
    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    ready_event = asyncio.Event()
    
    task1 = asyncio.create_task(
        TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv,
                LoGinDaTaUncRypTinG, ready_event, region)
    )
    
    await ready_event.wait()
    await asyncio.sleep(1)
    
    task2 = asyncio.create_task(
        TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen)
    )
    
    os.system('clear')
    print(render('DEV', colors=['white', 'green'], align='center'))
    print(f"\n - BoT STarTinG And OnLine on TarGet : {TarGeT} | BOT NAME : {acc_name}")
    print(" - BoT sTaTus > GooD | OnLinE ! (:  - FASTAPI VERSION")
    print(" - API Docs: http://localhost:10000/docs\n")
    
    await asyncio.gather(task1, task2)

async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout=7 * 60 * 60)
        except asyncio.TimeoutError:
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e:
            print(f"ErroR TcP - {e} => ResTarTinG ...")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(StarTinG())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host='0.0.0.0', port=port, log_level="info")
