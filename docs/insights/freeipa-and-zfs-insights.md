in proxmox pve i want to create a zpool mirror from two usb ssd disks. should i enabkle compression? should i modify the ashift? the disks are samsung t7 2TB ssd.

For a ZFS zpool mirror on two Samsung T7 2TB SSDs connected via USB, you should enable compression and set the `ashift` value to 12.

-----

### Compression

**ZFS compression** is a feature that reduces the amount of data written to disk, which in turn can improve both disk lifespan and performance. The most recommended compression algorithm for ZFS is **LZ4**. It's very fast, has low CPU overhead, and the performance gain from reduced I/O often outweighs the minimal CPU usage. Furthermore, ZFS is intelligent and won't compress data that is already compressed (e.g., video files or JPEGs), so you get the benefits where possible without wasting resources on incompressible data.

-----

### Ashift Value

The `ashift` parameter in ZFS defines the sector size (2^ashift) that the pool will use. For modern SSDs like the Samsung T7, the physical block size is 4K or larger, even if they report a smaller 512B logical sector size for compatibility.

Setting `ashift=12` (2^12 = 4096 bytes or 4K) ensures that ZFS aligns its I/O with the physical block size of the SSD. If you use the default `ashift=9` (512B), which is often the logical block size reported by the disk, ZFS would perform multiple I/O operations to write a single 4K block. This can lead to significant **write amplification**, which degrades performance and shortens the lifespan of the SSD. By setting `ashift=12`, you avoid this performance penalty and ensure your pool operates efficiently. The `ashift` value cannot be changed after the pool is created, so it is crucial to set it correctly from the start.

\<br\>
When setting up a ZFS pool, this video shows how to create a ZFS pool inside Proxmox using two USB drives.

While it doesn't matter for ZFS itself, using **hyphens** is generally better. The ZFS command-line tools and the underlying filesystem support both hyphens (`-`) and underscores (`_`) in pool and dataset names. Both `freeipa-mirror` and `freeipa_mirror` are perfectly valid.

---

does it matter if the pool name contains hyphens? e.g. freeipa-mirror 
or is it better to use underscores? e.g. freeipa_mirror

### Why Hyphens Are Preferred

The choice between hyphens and underscores is more of a convention or best practice, particularly in a Linux environment.

* **Command-line parsing:** Hyphens are often treated as word separators by many command-line utilities and text editors. This allows you to easily select an entire name like `freeipa-mirror` with a double-click, whereas `freeipa_mirror` would be treated as a single, contiguous word. This is a small but useful quality-of-life improvement for administration.

* **Consistency:** Many Linux system services and configurations, including Proxmox itself, use hyphens as standard separators in their naming conventions (e.g., `pve-cluster`, `pve-ha-manager`). Following this convention makes your naming scheme more consistent with the rest of the system.

* **Readability:** For some, hyphens provide better visual separation and readability than underscores, making long names easier to scan.

In summary, there is no functional difference in ZFS. Use whichever you prefer, but hyphens are a widely accepted convention in the Linux world for good reason.

---

is it better to choose mirror or raidz10? i imagine that they aare the same in this case?

For your setup of two disks, a ZFS **mirror** is the only correct choice. RAIDZ10 is a different configuration and is not possible with just two disks.

---

### Mirror vs. RAIDZ10

* **ZFS Mirror:** A mirror requires at least two disks. It's the ZFS equivalent of RAID 1, where all data is written identically to both drives. This provides **redundancy** against a single drive failure and can improve read performance as ZFS can read from either disk. With two disks, a mirror is the only redundant ZFS topology you can create.

* **ZFS RAIDZ10:** This is a hybrid ZFS topology that combines the concepts of RAID 10 (mirroring and striping). It's a pool made up of multiple mirrored vdevs (virtual devices) that are then striped together. For example, a RAIDZ10 setup with four disks would be two mirrored pairs, where data is then striped across both pairs. The main advantage of this setup is a significant boost in performance, especially for random I/O, as it combines the speed of striping with the redundancy of mirroring. A RAIDZ10 setup requires at least **four disks** (two mirrored pairs).

In your case, with only two disks, you can only create a ZFS mirror. The performance and redundancy of a two-disk ZFS mirror are excellent for most use cases, especially with fast SSDs.

---
Here is a video from YouTube that explains the performance differences between ZFS mirrors and RAIDZ.