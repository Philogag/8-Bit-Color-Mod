package com.philogag.fcbm;

import com.philogag.fcbm.proxy.CommonProxy;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.SidedProxy;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPostInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import org.apache.logging.log4j.Logger;

@Mod(modid = FullColorMod.MODID, name = FullColorMod.NAME, version = FullColorMod.VERSION)
public class FullColorMod
{
    public static final String MODID = "fcbm";
    public static final String NAME = "Full Color Block Mod";
    public static final String VERSION = "Beta: 1.0";

    // 主类实例
    @Mod.Instance(FullColorMod.MODID)
    public static FullColorMod instance;

    // 代理实例
    @SidedProxy(clientSide = "com.philogag.fcbm.proxy.ClientProxy",
            serverSide = "com.philogag.fcbm.proxy.CommonProxy")
    public static CommonProxy proxy;

    // 日志实例
    public static Logger logger;

    @EventHandler
    public void preInit(FMLPreInitializationEvent event) {
        logger = event.getModLog();
        proxy.preInit(event); // 通过代理注册物品与方块
        logger.info("Mod Load");
    }

    @EventHandler
    public void init(FMLInitializationEvent event) {
        proxy.init(event);
    }

    @EventHandler
    public void postInit(FMLPostInitializationEvent event) {
        proxy.postInit(event);
    }
}