prog _generated-binaries_variant1_kocher_ex1_x86_64 {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	rax, qword ptr [rbp - 8];
    4194316c:	cmp	rax, qword ptr [0x400008];
    4194324:	jae	0x400045;
ENTRY_4194384:
    4194384:	push	rbp;
    4194385:	mov	rbp, rsp;
    4194388:	pop	rbp;
    4194389:	ret;
ENTRY_4194330:
    4194330a:	mov	rax, qword ptr [rbp - 8];
    4194334e:	movzx	ecx, byte ptr [rax + 0x400001];
    4194342:	shl	ecx, 9;
    4194345:	movsxd	rax, ecx;
    4194348c:	movzx	ecx, byte ptr [rax + 0x400001];
    4194356:	movzx	edx, byte ptr [0x400001];
    4194364c:	and	edx, ecx;
    4194366e:	mov	byte ptr [0x400001], dl;
    4194373:	pop	rbp;
    4194374:	ret;
ENTRY_4194373:
    4194373:	pop	rbp;
    4194374:	ret;
ENTRY_4194375:
    4194375:	nop	word ptr [rax + rax];
}
